import logging

logger = logging.getLogger('InvApp')

logger.setLevel(logging.INFO)

handler = logging.FileHandler('logs.log', 'w')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('% (levelname)s - %(asctime)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
