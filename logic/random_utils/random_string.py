import os
import string, random
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def random_string(length: int, chars: str = None) -> str:
    """
    Returns a random string of given length.
    
    Args:
        length (int): Desired length of the string.
        chars (str, optional): Characters to use. Defaults to letters+digits.
        
    Returns:
        str: Random string.
    """
    
    if chars is None:
        chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def patterned_string(pattern: str) -> str:
    """
    Returns a string following a pattern.
    'L' -> uppercase letter, 'l' -> lowercase, 'd' -> digit
    
    Example:
        pattern = "Ll-dd" -> "Ab-47"
    """
    
    result = ""
    for p in pattern:
        if p == "L":
            result += random.choice(string.ascii_uppercase)
        elif p == "l":
            result += random.choice(string.ascii_lowercase)
        elif p == "d":
            result += random.choice(string.digits)
        else:
            result += p
    return result


def shuffle_string(s: str) -> str:
    """
    Returns a shuffled version of the string.
    """
    
    lst = list(s)
    random.shuffle(lst)
    return ''.join(lst)


def random_dni() -> str:
    """
    Generates a random valid Spanish DNI.
    
    Returns:
        str: DNI in the format '12345678Z' with correct letter.
    """
    
    numero = random.randint(0, 99999999)
    numero_str = f"{numero:08d}"  # rellena con ceros a la izquierda

    # Calcular la letra
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra = letras[numero % 23]

    return numero_str + letra

