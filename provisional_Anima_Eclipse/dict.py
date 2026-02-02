import random
import os, sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from status import ElementStatus

growth_dict: dict[str, str] = {
    "fast": "growth = 4 * lvl**3 / 5",
    "normal": "growth = lvl**3",
    "slow": "growth = 5 * lvl**3 / 4",
    "parabolic": "growth = 6 * lvl**3 / 5 - 15 * lvl**2 + 100 * lvl -140",
}
'''Possible growth forms for the Animas'''

formula_dict: dict[str, str] = {
    "hp": "hp = (lvl/100 * ((stat_base*2) + potential)) + lvl",
    "stat": "stat = (5 + (lvl/100 * ((stat_base*2) + potential))) * nature",
    "catch": "catch = (hp_max*3 - hp_now*2) * catch_ratio * ball_ratio/hp_max*3 * status",
    "damage": f"damage = (stab * eff * {random.randint(75, 100)} * (((1/5 * lvl +1) * atk * power) / (25 * def) + 2)) / 100",
    "exp_given": "exp_given = (exp_base_given*lvl/participants/5) * ((2*lvl+10)**(5/2)) / ((lvl+ally_lvl+10)**(5/2)) + 1) * combat_type * object_mod * arcana_mod", #VERIFICAR FORMULA
                 # combat_type: si es wild 1 si no 1.5
    "growth": growth_dict,
    "hit_chance": "hit_chance = move_accuracy * (attacker_accuracy/defender_evasion) / 100", 
                  # Este número sera el que se use cuando se verifique en combate, con uno random del 0 al 1, si es mayor o igual a ese random entonces le da
}
'''A bunch of formulas'''


arcana_mod_dict = {
    0: 1,
    1: 1.1,
    2: 1.2,
    3: 1.3,
    4: 1.4,
    5: 1.5,
    6: 1.6,
    7: 1.7,
    8: 1.8,
    9: 1.9,
    10: 2, 
}
'''The dictionary to know the multiplier when recieving xp depending on the level of confident of that arcana'''


stat_inc_dec_dict: dict[int, float] = {
    -6: 2/8,
    -5: 2/7,
    -4: 2/6,
    -3: 2/5,
    -2: 2/4,
    -1: 2/3,
    0: 2/2,
    1: 3/2,
    2: 4/2,
    3: 5/2,
    4: 6/2,
    5: 7/2,
    6: 8/2
}
'''A dictionary that contains the min and max increases/decreases a regular stat can have (atk, sp atk, def, sp def, spe)'''

critical_index_dict: dict[int, float] = {   
    0: 0.0625,
    1: 0.125,
    2: 0.25,
    3: 0.333,
    4: 0.5,
    5: 0.75,
    6: 1
}
'''A dictionary that contains the critical hit chance percentages based on the index'''