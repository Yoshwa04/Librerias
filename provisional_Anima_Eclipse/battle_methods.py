from anima import Anima
from logic.math_core.solver import give_just_one_solution, solve_equation
from player import Player
from dict import arcana_mod_dict, formula_dict


# PROVISIONAL

def calc_exp(player: Player, anima: Anima, combat_type: float):
    for confident in player.confidents:
        arcana_lvl = confident.lvl if anima.arcana == confident.arcana else arcana_lvl = 0
        
    arcana_mod = arcana_mod_dict.get(arcana_lvl)
    object_mod = 1.5 if anima.object == "lucky_egg" else object_mod = 1
    
    return int(give_just_one_solution(solve_equation(formula_dict["exp_given"], f"exp_base_given = {anima.exp_base_given}", f"lvl = {anima.lvl}", f"participants = ", f"ally_lvl = ", f"combat_type = {combat_type}", f"object_mod = {object_mod}", f"arcana_mod = {arcana_mod}"), "exp_given"))  
    