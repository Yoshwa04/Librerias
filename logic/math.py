from typing import List, Dict, Union, Any
from sympy import symbols, Eq, solve, sympify

class Constants():
    '''This class just contains some mathematic constants'''
    
    PI = 3.14159265358979323846
    E = 2.71 
    '''Euler'''
    C = 299792458
    '''Light Speed'''
    DEGREES_TO_RADIANS = 0.017453292519943295
    RADIANS_TO_DEGREES = 57.29577951308232
    
    
formula_list = {
}


def solve_equation(*eq_given : str) -> Union[List[Dict[str, Any]], str]:
    """This method solves the given equation/s with the most exactitude possible. When theres no enough equations for the existing incognites in that equations it just reduces the length at its maximum.

    Returns:
          Union[List[Dict[str, Any]], str]: A list of solution dictionaries or an error message.
    """
    
    try:
        eq_sym = []
        for i in eq_given:
            left, right = i.split("=")
            left = left.strip()
            right = right.strip()
            eq = Eq(sympify(left), sympify(right))
            eq_sym.append(eq)

        var = sorted(set().union(*[eq.free_symbols for eq in eq_sym]), key=lambda l: l.name)

        return solve(eq_sym, *var, dict=True)
    except Exception as e:
        return f"Error: {e}"

def give_just_one_solution(solutions: list[Dict[Any, Any]], solution: str) -> Any:
    """Returns the value of a specific variable from the first solution in a list of SymPy solutions.

    Args:
        solutions (list[Dict[Any, Any]]): A list of solution dictionaries.
        solution (str): The name of the variable whose value should be extracted. 

    Returns:
        Any: The value associated with the requested variable in the first solution. 
            The returned type depends on SymPy and may be an integer, float, Rational, 
            symbolic expression, or any other SymPy-compatible type.
    """

    return solutions[0][symbols(solution)]
