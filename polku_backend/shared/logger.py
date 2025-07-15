import sys
import logging

from loguru import logger

logger.remove()

# logger format
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

# logger for console messages in development
logger.add(
    sys.stderr,
    level="DEBUG",
    format=log_format,
    colorize=True,
)

# logger file for production
logger.add(
    "logs/polku_app.log",
    level="INFO",
    format="{time} {level} {message}",
    rotation="2 MB",
    retention=5,
    compression="zip",
    serialize=False,
)

# class defined too intercep log messages from pỳthon logging
class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Obtener el nivel de loguru correspondiente
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Encontrar el frame correcto en el stack
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )



