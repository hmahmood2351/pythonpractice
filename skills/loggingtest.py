import logging 
import traceback
from logging.handlers import RotatingFileHandler

logname = logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

import helper


logging.debug('Debug msg')
logging.info('informational msg')
logging.warning('Warning msg')
logging.error('Error msg')
logging.critical('Critical msg')


try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error("The error is %s", traceback.format_exc())
    logging.error(e, exc_info=True)