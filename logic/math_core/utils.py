from sympy import simplify, sympify


def is_valid_expression(expr: str) -> bool:
    try:
        sympify(expr)
        return True
    except:
        return False

def simplify_expression(expr: str) -> str:
    return simplify(sympify(expr))