import os
import random
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.math import give_just_one_solution, solve_equation
from itertools import count

# n = random.randint(1, 100)
# n2 = int(give_just_one_solution(solve_equation("hit_chance = 25 * ((2/2)/(2/2))"), "hit_chance"))
# bol = True if n2 >= n else False
# print(n, n2, bol)


# n = int(give_just_one_solution(solve_equation(f"damage = (3/2 * 1/2 * 85 * (((1/5 * 100 +1) * 410 * 150) / (25 * def) + 2)) / 100"), "damage"))
# print(n)


n = count(0)

print(str(next(n)))
print(str(next(n)))