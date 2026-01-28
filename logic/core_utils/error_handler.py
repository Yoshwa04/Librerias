import logging
from typing import Callable, Any

def safe_execute(func: Callable[..., Any], *args, logger: logging.Logger = None, **kwargs) -> Any:
    """
    Executes a function safely, catching exceptions.

    Args:
        func: The function to execute.
        *args: Positional arguments to pass to the function.
        logger: Optional logger to log the error.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        Any: The result of the function if successful, None otherwise.
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        if logger:
            logger.error(f"Error in {func.__name__}: {e}", exc_info=True)
        else:
            print(f"Error in {func.__name__}: {e}")
        return None
