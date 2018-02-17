import logging
from datetime import datetime
Logger=logging
LEVELS = { 'debug':logging.DEBUG,
            'info':logging.INFO,
            'warning':logging.WARNING,
            'error':logging.ERROR,
            'critical':logging.CRITICAL,
            }
logging.basicConfig(filemode='w',filename='worldLogging'+str((datetime.now()).strftime('%Y_%m_%d'))+'.log',level=LEVELS.get('info', logging.NOTSET))
#_%H_%M