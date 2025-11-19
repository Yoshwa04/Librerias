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


def solve_equation(*eq_given : str):
    '''
        This method solves the given equation/s with the most exactitude possible. 
        When theres no enough equations for the existing incognites in that equations it just reduces the length at its maximum.
    '''
    
    try:
        eq_sym = []
        for i in eq_given:
            left, right = i.split("=")
            eq = Eq(sympify(left), sympify(right))
            eq_sym.append(eq)

        var = sorted(set().union(*[eq.free_symbols for eq in eq_sym]), key=lambda l: l.name)

        return solve(eq_sym, *var, dict=True)
    except Exception as e:
        return f"Error: {e}"

def give_just_one_solution(solutions: list, solution: str) :
    return solutions[0][symbols(solution)]
# res = solve_equation("x = 643/2")
# x = symbols('x')

# value = res[0][x]

# print(int(value))
