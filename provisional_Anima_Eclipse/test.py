import os
from random import randint
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.math import give_just_one_solution, solve_equation

n = randint(1, 100)
n2 = give_just_one_solution(solve_equation("hit_chance = 50 * (4/2/1)"), "hit_chance")
bol = True if n2 >= n else False
print(n, n2, bol)