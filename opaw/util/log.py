import logging

levels = {
    "d": logging.DEBUG,
    "i": logging.INFO,
    "w": logging.WARNING,
    "e": logging.ERROR,
    "c": logging.CRITICAL,
}


def get(name, file="./log.log"):
    from opaw.util import mkdirs, create_file

    """
    Gets a logger with the given name (singleton)
    :param name: logger name
    :param file: the file logs will be saved (default: ./log.log)
    """
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        # make parent dirs if needed
        create_file(file)

        # stream handler
        stream_formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

        # file handler
        file_handler = logging.FileHandler(file, mode="w", encoding="utf-8")
        file_formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s(%(name)s) %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # set default level to info
        set_level(name, "i")

    return logger


def set_level(name, level):
    """
    Sets the log level of the logger and handlers with the given name
    :param name: logger name
    :param level: log level (d: debug, i: info, w: warning, e: error, c: critical)
    """
    level = levels[level]
    logger = logging.getLogger(name)
    logger.setLevel(level)
    for hander in logger.handlers:
        hander.setLevel(level)
