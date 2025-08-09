import os
import logging

print(os.name)

logger = logging.getLogger("MAIN")
logger.error('Error happened in app while processing images')