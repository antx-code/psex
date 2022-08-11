from loguru import logger
import yaml
import os


@logger.catch(level='ERROR')
def weak_passwords(db: str):
    base_path = os.path.dirname(__file__)
    logger.debug(f'[+] Selecting {db} weak passwords.')
    with open(f'{base_path}/{db}.yaml', 'r+', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config['passwords']
