# utils/logger.py
from loguru import logger
import sys

def setup_logger():
    logger.remove()
    logger.add(sys.stdout, level="INFO")
    logger.add("logs/crewai_tiktok.log", rotation="1 MB", level="DEBUG")
    return logger

log = setup_logger()