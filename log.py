import logging

FORMAT = "%(filename)s[%(lineno)d];" \
             " %(levelname)s [%(asctime)s] %(message)s"
FILE = 'log.log'

global logger

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
fh = logging.FileHandler(FILE)
fh.setLevel(logging.NOTSET)
fh.setFormatter(formatter)
logger.addHandler(fh)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


if __name__ == "__main__":
    logger.debug('my test')
