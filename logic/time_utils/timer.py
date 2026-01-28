import time

def start_timer() -> float:
    return time.time()


def stop_timer(start_time: float) -> float:
    return time.time() - start_time


def measure_execution(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start
