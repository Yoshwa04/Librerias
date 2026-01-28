# logger.py
import logging
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO, logfile: Optional[str] = None) -> logging.Logger:
    """
    Sets up and returns a logger.

    Args:
        name: The name of the logger.
        level: Logging level (DEBUG, INFO, WARNING, etc.).
        logfile: Optional file path to save logs.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler (optional)
    if logfile:
        fh = logging.FileHandler(logfile)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
