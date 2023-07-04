from loguru import logger
import csv
import os
from pocx.funcs import Fofa


class AssetIO():
    def __init__(self):
        pass

    @logger.catch(level='ERROR')
    def get_fofa_assets(self, grammar: str, fofa_key: str, fofa_email: str, to_file: str = None):
        assets = []
        fofa = Fofa()
        fofa.set_config(api_key=fofa_key, api_email=fofa_email)
        logger.warning(f'[+] the asset account of grammar: {grammar} are: {fofa.asset_counts(grammar)}')
        pages = fofa.asset_pages(grammar)
        for page in range(1, pages + 1):
            logger.info(f'[*] page {page}')
            urls = fofa.assets(grammar, page)
            for url in urls:
                asset = url.strip().split('//')[1]
                assets.append(asset)
                if to_file:
                    base_path = os.getcwd()
                    if not os.path.exists(f'{base_path}/input'):
                        os.mkdir(f'{base_path}/input')
                    with open(f'{base_path}/input/{to_file}', 'a+') as f:
                        f.write(asset + '\n')
        return assets

    @logger.catch(level='ERROR')
    def get_file_assets(self, filename: str):
        assets = []
        with open(filename, 'r+') as f:
            ips = f.readlines()
        for asset in ips:
            assets.append(asset.strip())
        assets = list(set(assets))
        return assets

    @logger.catch(level='ERROR')
    def save2file(self, filename: str, ip: str, port: int, username: str, password: str):
        username = '空' if username == '' else username
        password = '空' if password == '' else password
        base_path = os.getcwd()
        if not os.path.exists(f'{base_path}/output'):
            os.mkdir(f'{base_path}/output')
        target_file_path = f'{base_path}/output/{filename}.csv'
        fieldnames = ['IP', 'Port', 'Username', 'Password']
        content = {
            'IP': ip,
            'Port': port,
            'Username': username,
            'Password': password
        }
        with open(target_file_path, 'a+', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if os.path.getsize(target_file_path) == 0:
                writer.writeheader()
            writer.writerow(content)
            f.close()
