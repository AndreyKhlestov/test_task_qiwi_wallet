import logging
import sys


def get_stream_handler(formatter: logging.Formatter) -> logging.StreamHandler:
    """Консольный обработчик"""
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    return stream_handler
