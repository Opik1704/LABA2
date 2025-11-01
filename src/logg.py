import logging
import os

def make_logger():
    """
    создает логгер
    :return: возвращает логер
    """
    logging.basicConfig(level=logging.INFO, filename="shell.log",filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")
    logger = logging.getLogger("shell")
    logger.setLevel(logging.INFO)
    if os.path.exists("shell.log"):
        logger.info("--- Новая сессия ---")
    else:
        logger.info("--- Первая сессия, файл логов создан ---")
    return logger
