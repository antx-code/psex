from loguru import logger
import yaml
import os


@logger.catch(level='ERROR')
def weak_passwords(db: str):
    base_path = os.path.dirname(__file__)
    try:
        with open(f'{db}.yaml', 'r+', encoding='utf-8') as f:
            logger.warning(f'[+] Selecting {db} weak passwords.')
            config = yaml.safe_load(f)
    except FileNotFoundError:
        with open(f'{base_path}/{db}.yaml', 'r+', encoding='utf-8') as f:
            logger.debug(f'[+] Selecting {db} weak passwords.')
            config = yaml.safe_load(f)
    return config['passwords']
