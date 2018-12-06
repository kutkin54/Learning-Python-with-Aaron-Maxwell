import logging
mode = 'production'
log_file = 'myapp.log'
if mode == 'developemnt':
    log_level = logging.DEBUG
    log_mode = 'w'
else:
    log_level = logging.WARNING
    log_mode = 'a'
logging.basicConfig(level=log_level, filename=log_file, filemode=log_mode)
logging.debug('debug messagge')
logging.warning('LOOK OUT')
logging.critical('we have a problem here')
