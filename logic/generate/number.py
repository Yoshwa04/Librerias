from random import randint

def randfloat(a: int, b: int) -> float:
    """Returns a random float in between two integers

    Args:
        a (int): the starting integer 
        b (int): the final integer

    Returns:
        float: a random float
    """
    
    return randint(a, b) + (randint(0, 99)/100)
