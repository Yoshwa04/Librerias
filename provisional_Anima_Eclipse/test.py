import os
import random
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.math import give_just_one_solution, solve_equation
from itertools import count

# n = random.randint(1, 100)
# n2 = give_just_one_solution(solve_equation("hit_chance = 50 * ((2/2)/(8/2))"), "hit_chance")
# bol = True if n2 >= n else False
# print(n, n2, bol)

n = count(98)

def efe() -> str:
    return str(next(n)).zfill(3)

print(efe())
print(efe())
print(efe())
print(efe())