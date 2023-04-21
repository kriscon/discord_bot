import functools
import logging
from typing import Any, Callable

def with_logging(func: Callable[..., Any]):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info('Calling %s', func.__name__)
        value = func(*args, **kwargs)
        logging.info('Finished calling %s', func.__name__)
        return value

    return wrapper

# add dot notation for dicts (e.g. dict.item instead of dict['item'])
class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
