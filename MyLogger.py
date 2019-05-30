import logging
from logging import handlers


class MyLogger:
    __level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename='log.txt', level='debug', fmt='%(asctime)s - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)

        self.logger.setLevel(self.__level_relations.get(level))
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)

        th = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=3,
                                               encoding='utf-8')

        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


if __name__ == '__main__':
    log = MyLogger('test.log', level='debug')
    log.logger.warning('Test')
    log.logger.error('Test')
    log.logger.info('Test')
    log.logger.critical('Test')
    log.logger.debug('Test')