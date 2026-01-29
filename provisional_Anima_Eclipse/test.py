import os
import random
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.random_utils.random_number import randfloat

from logic.math_core.solver import give_just_one_solution, solve_equation
from itertools import count


# n = int(randfloat(0, 1) * 100) / 100
# n2 = int(give_just_one_solution(solve_equation("hit_chance = 100 * ((8/2)/(2/8)) / 100"), "hit_chance"))
# bol = True if n2 >= n else False
# print(n, n2, bol)


# n = int(give_just_one_solution(solve_equation(f"damage = (3/2 * 1/2 * 85 * (((1/5 * 100 +1) * 410 * 150) / (25 * def) + 2)) / 100"), "damage"))
# print(n)