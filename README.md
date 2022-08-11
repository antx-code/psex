# psex
A simple, fast and powerful password scanner engine tool was built by antx.

## Description
psex is a simple, fast and powerful password scanner engine tool was built by antx. psex also 
support some useful features, which like fofa search and parse assets to verify. psex has been built in some weak username and password. 

## Install

```bash
pip3 install psex
```

## Usage

### PSE Sample:

```python
# Title: xxxxxxx
# Author: antx
# Email: wkaifeng2007@163.com

from loguru import logger
from redis import Redis
from psex import ScannerEngine
from psex.funcs.assetio import AssetIO
from psex.weaks import weak_passwords


class Scanner(ScannerEngine):
    def __init__(self):
        super(Scanner, self).__init__()

    @logger.catch(level='ERROR')
    def is_connected(self, connection):
        """
        check if the connection is connected.
        """
        try:
            connection.ping()
            return True
        except Exception as e:
            return False

    @logger.catch(level='ERROR')
    def create_connect(self, *args):
        """
        
        create a connection.
        
        """
        connection = Redis(host=args[0], port=args[1], password=args[3], db=0, socket_connect_timeout=self.timeout,
                           socket_timeout=self.timeout)
        return connection

    @logger.catch(level='ERROR')
    def dia(self):
        asset_io = AssetIO()
        ips = asset_io.get_file_assets('source_redis.csv')
        passwords = weak_passwords('redis')
        for password in passwords:
            for ip_port in ips:
                ip_port = ip_port.strip()
                ip = ip_port.split(':')[0]
                port = int(ip_port.split(':')[1])
                logger.debug(f'Connecting to {ip} ......')
                logger.warning(f'Testing {ip_port} with password: "{password}" !')
                result = self.poc(ip, port, '', password)
                if result:
                    asset_io.save2file('redis_success', ip, port, '', password)


if __name__ == '__main__':
    ds = Scanner()
    ds.dia()
```
