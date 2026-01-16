import string
from typing import List, Dict, Optional, Union, Any
from sympy import symbols, Eq, solve, sympify

class Constants():
    '''This class just contains some mathematic constants'''
    
    PI = 3.14159265358979323846
    E = 2.71828
    '''Euler'''
    C = 299792458
    '''Light Speed'''
    DEGREES_TO_RADIANS = 0.017453292519943295
    RADIANS_TO_DEGREES = 57.29577951308232
    
    
formulas = {
}


def solve_equation(*eq_given : str) -> Union[List[Dict[str, Any]], str]:
    """This method solves the given equation/s with the most exactitude possible. When theres no enough equations for the existing incognites in that equations it just reduces the length at its maximum. If no incognite given but only the operation, it will assign automatically it starting with x, y, z then a, b, c.... then x2, y2, z2...

    Returns:
          Union[List[Dict[str, Any]], str]: A list of solution dictionaries or an error message.
    """
    
    try:
        eq_sym = []
        auto_vars = list('xyz') + [c for c in string.ascii_lowercase if c not in 'xyz']
        auto_index = 0
        for i, expr in enumerate(eq_given):
            expr = expr.strip()
            if expr == "":
                return "The equations must have at least 1 number or another incognite"
            
            if "=" not in expr:
                if auto_index < len(auto_vars):
                    var_name = auto_vars[auto_index]
                else:
                    var_name = auto_vars[auto_index % len(auto_vars)] + str(auto_index // len(auto_vars)+1)
                expr = f"{var_name} = {expr}"
                auto_index += 1
            
            left, right = expr.split("=")
            left = left.strip()
            right = right.strip()
            eq = Eq(sympify(left), sympify(right))
            eq_sym.append(eq)

        var = sorted(set().union(*[eq.free_symbols for eq in eq_sym]), key=lambda l: l.name)

        return solve(eq_sym, *var, dict=True)
    except Exception as e:
        return f"Error: {e}"

def give_just_one_solution(solutions: list[Dict[Any, Any]], solution: Optional[str] = None) -> Any:
    """Returns the value of a specific variable from the first solution in a list of SymPy solutions.

    Args:
        solutions (list[Dict[Any, Any]]): A list of solution dictionaries.
        solution (str): The name of the variable whose value should be extracted. Defaults to None

    Returns:
        Any: The value associated with the requested variable, or the first value if no variable is specified. Can be an integer, a float...
    """

    if not solutions:
        return "The method needs to be provided of at least one solution."
    
    first_solution = solutions[0]
    
    if solution is not None:
        return first_solution[symbols(solution)]
    else:
        return next(iter(first_solution.values()))