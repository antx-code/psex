from abc import ABCMeta, abstractmethod
from loguru import logger


class ScannerEngine(metaclass=ABCMeta):
    @logger.catch(level='ERROR')
    def __init__(self):
        self.mode = 'Synchronous Mode'
        self.name = "Password Scanner Engine(PSE)"
        self.timeout = 3
        self.timeout_ms = 3000
        logger.info(f'Testing {self.name} with {self.mode}.')

    @abstractmethod
    @logger.catch(level='ERROR')
    def is_connected(self, connection) -> bool:
        pass

    @abstractmethod
    @logger.catch(level='ERROR')
    def create_connect(self, *args):
        pass

    @logger.catch(level='ERROR')
    def poc(self, *args):
        connection = self.create_connect(*args)
        if not connection:
            logger.error('Connection failed, create connection error!')
            return False
        if not self.is_connected(connection):
            logger.error('Connection failed, authentication error!')
            return False
        else:
            logger.success('Connection successful, authentication success!')
            return True

    @logger.catch(level='ERROR')
    def run(self, *args):
        args = [args] if isinstance(args[0], str) else args[0]

        for arg in args:
            self.poc(*arg)
