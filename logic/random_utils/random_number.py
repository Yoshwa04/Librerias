from random import gauss, randint, random, uniform


def randunit() -> float:
    """Returns a random float between 0.0 and 1.0"""
    
    return random()

def randfloat(a: float, b: float) -> float:
    """
    Returns a uniformly distributed random float between a and b.
    """
    
    return a + (b - a) * random()


def randrange_float(start: float, stop: float, step: float) -> float:
    """
    Returns a random float with a fixed step.
    """
    
    steps = int((stop - start) / step)
    return start + randint(0, steps) * step


def uniform_float(a: float, b: float) -> float:
    """Uniform distribution"""
    
    return uniform(a, b)


def gaussian(mean: float = 0.0, std_dev: float = 1.0) -> float:
    """Normal (Gaussian) distribution"""
    
    return gauss(mean, std_dev)

def bounded(mean: float, deviation: float, min_val: float, max_val: float) -> float:
    """
    Returns a bounded random number.
    """
    
    value = gauss(mean, deviation)
    return max(min_val, min(max_val, value))


def normalized(value: float, min_val: float, max_val: float) -> float:
    """
    Normalizes a value to the range [0, 1].
    """
    
    return (value - min_val) / (max_val - min_val)