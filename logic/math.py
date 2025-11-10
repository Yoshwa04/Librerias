from sympy import symbols, Eq, solve, sympify

class Constants():
    PI = 3.14159265358979323846
    E = 2.71 # Euler
    C = 299792458 # Light Speed
    DEGREES_TO_RADIANS = 0.017453292519943295
    RADIANS_TO_DEGREES = 57.29577951308232

def solve_equation(*eq_given):
    try:
        eq_sym = []
        for i in eq_given:
            izquierda, derecha = i.split("=")
            eq = Eq(sympify(izquierda), sympify(derecha))
            eq_sym.append(eq)

        var = sorted(set().union(*[eq.free_symbols for eq in eq_sym]), key=lambda l: l.name)

        return solve(eq_sym, *var, dict=True)
    except Exception as e:
        return f"Error: {e}"
    
# res = solve_equation("x = 643/2")
# x = symbols('x')

# value = res[0][x]

# print(int(value))
