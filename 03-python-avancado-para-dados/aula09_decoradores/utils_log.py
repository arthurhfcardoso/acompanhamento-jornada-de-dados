from functools import wraps

from loguru import logger

logger.remove()

logger.add(
    "meu_arquivo_de_logs.log",
    format="{time} {level} {message} {file}",
    level="INFO",
)

logger.add(
    "meu_arquivo_de_logs_critial.log",
    format="{time} {level} {message} {file}",
    level="CRITICAL",
)


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        message = (
            f"Chamando funcao '{func.__name__}' com args {args} "
            f"e kwargs {kwargs}"
        )
        logger.info(message)
        try:
            result = func(*args, **kwargs)
            logger.info(f"Funcao '{func.__name__}' retornou {result}")
            return result
        except Exception as exc:
            logger.exception(f"Excecao capturada em '{func.__name__}': {exc}")
            # Re-raise to keep the original behavior of the decorated function.
            raise

    return wrapper
