import logging

format = "%(name)s[%(process)d] %(levelname)s %(message)s"

logging.basicConfig(level=logging.INFO, format=format)

logger = logging.getLogger("whatsbot")
logger.setLevel(logging.INFO)