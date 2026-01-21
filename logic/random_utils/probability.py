from random import choice, choices, randint, random, seed


def chance(probability: float) -> bool:
    """
    Returns True with a given probability.

    Args:
        probability (float): A value between 0.0 and 1.0 representing
                             the chance of returning True.

    Returns:
        bool: True with the given probability, False otherwise.

    Raises:
        ValueError: If probability is not between 0 and 1.
    """
    
    if not 0 <= probability <= 1:
        raise ValueError("Probability must be between 0 and 1")
    return random() < probability

def increasing_chance(attempt: int, base: float = 0.1, cap: float = 1.0) -> bool:
    """
    Returns True with a probability that increases linearly
    with each attempt until a maximum cap is reached.

    Commonly used for retry systems, loot drops, or critical chances.

    Args:
        attempt (int): Number of attempts made so far.
        base (float): Base probability increase per attempt.
        cap (float): Maximum allowed probability.

    Returns:
        bool: True or False based on the calculated probability.
    """
    
    probability = min(base * attempt, cap)
    return chance(probability)


def fifty_fifty() -> bool:
    """
    Returns True or False with equal probability (50%).

    Returns:
        bool: Random boolean value.
    """
    
    return chance(0.5)


def roll(dice: int = 6) -> int:
    """
    Simulates rolling a dice.

    Args:
        dice (int): Number of sides of the dice. Defaults to 6.

    Returns:
        int: A random integer between 1 and dice (inclusive).
    """
    
    return randint(1, dice)

def roll_range(min_val: int, max_val: int) -> int:
    """
    Returns a random integer within a specified range.

    Args:
        min_val (int): Minimum value (inclusive).
        max_val (int): Maximum value (inclusive).

    Returns:
        int: A random integer between min_val and max_val.
    """
    
    return randint(min_val, max_val)


def weighted_bool(true_weight: int, false_weight: int) -> bool:
    """
    Returns True or False based on weighted probabilities.

    Args:
        true_weight (int): Weight for returning True.
        false_weight (int): Weight for returning False.

    Returns:
        bool: True or False according to the given weights.
    """
    
    total = true_weight + false_weight
    return randint(1, total) <= true_weight

def weighted_choice(options: list, weights: list):
    """
    Selects a random element from a list using weighted probabilities.

    Args:
        options (list): List of selectable values.
        weights (list): List of weights corresponding to each option.

    Returns:
        Any: One randomly selected element from options.
    """
    
    return choices(options, weights=weights, k=1)[0]


def pick_one(*values):
    """
    Randomly selects one value from the given arguments.

    Args:
        *values: Any number of values to choose from.

    Returns:
        Any: One randomly selected value.
    """
    
    return choice(values)


def set_seed(value: int):
    """
    Sets the seed for the random number generator.

    Useful for reproducible results in testing or simulations.

    Args:
        value (int): Seed value.
    """
    
    seed(value)
    

def one_in(n: int) -> bool:
    """
    Returns True with a probability of 1 in n.

    Args:
        n (int): The inverse probability factor.

    Returns:
        bool: True with probability 1/n, False otherwise.

    Raises:
        ValueError: If n is less than or equal to 0.
    """
    
    if n <= 0:
        raise ValueError("n must be positive")
    return randint(1, n) == 1


