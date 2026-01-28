from anima import Anima
from logic.math_core.solver import *
from logic.random_utils.probability import chance
from player import Player
from dict import arcana_mod_dict, formula_dict, critical_index_dict, stat_inc_dec_dict
from category import Category
from technique import Technique
from type import effectiveness_chart
from constants import ELEMENT_STATUS_RESIDUAL_DAMAGE


# PROVISIONAL

# el lvl si es el del que has debilitado lo tengo que poner que se pase por parametro.
def calc_exp(player: Player, anima: Anima, foe_anima: Anima, combat_type: float) -> int:
    for confident in player.confidents:
        arcana_lvl = confident.lvl if anima.arcana == confident.arcana else arcana_lvl = 0
    
    arcana_mod = arcana_mod_dict.get(arcana_lvl)
    object_mod = 1.5 if anima.object == "lucky_egg" else object_mod = 1 # el objeto no se como se hará al final, de momento lo dejo como un str y ya
    
    return int(give_just_one_solution(solve_equation(formula_dict["exp_given"], f"exp_base_given = {foe_anima.exp_base_given}", f"lvl = {foe_anima.lvl}", f"participants = ", f"ally_lvl = ", f"combat_type = {combat_type}", f"object_mod = {object_mod}", f"arcana_mod = {arcana_mod}"), "exp_given"))  


# Esto se guardara en la logica del combate, para poder mandar el mensaje de ¡FALLAS / ESQUIVAS!... y tal
def calc_hit(anima_atk: Anima, anima_def: Anima, tech: Technique) -> bool:
    raw = give_just_one_solution(solve_equation(formula_dict["hit_chance"], f"move_accuracy = {tech.accuracy}", f"attacker_accuracy = {stat_inc_dec_dict[anima_atk.stats_inc_dec["acc"]]}", f"defender_evasion = {stat_inc_dec_dict[anima_def.stats_inc_dec["eva"]]}"), "hit_chance")
    
    hit_chance = max(0.0, min(1.0, raw))
    return chance(hit_chance)

def calc_crit(anima: Anima) -> bool:
    return chance(critical_index_dict[anima.crit_index])

# Se pasa el critico en boleano como parametro porque se tiene que saber fuera si ha sido critico, asi puedo mostrar un mensaje informando tipo ¡CRITICO! y tal 
def calc_direct_damage(anima_atk: Anima, anima_def: Anima, tech: Technique, critical: bool) -> int:
    stab = _calc_stab(anima_atk, tech)
    atk = _calc_atk(anima_atk, tech)
    def_ = _calc_def(anima_def, tech)
    eff = _calc_eff(anima_def, tech)
    
    crit = 1.5 if critical else 1
    
    return int(give_just_one_solution(solve_equation(formula_dict["damage"], f"stab = {stab}", f"eff = {eff}", f"lvl = {anima_atk.lvl}", f"atk = {atk}", f"power = {tech.power}", f"def = {def_}"), "damage") * crit)

def calc_residual_damage(anima: Anima):
    return int(anima.hp_max/ELEMENT_STATUS_RESIDUAL_DAMAGE)


def _calc_stab(anima: Anima, tech: Technique) -> float:
    return 1.5 if tech.type in (anima.type_a, anima.type_b1, anima.type_b2) else 1

def _calc_atk(anima: Anima, tech: Technique) -> float:
    return anima.atk * anima.stats_inc_dec["atk"] if tech.category == Category.PHYSICAL else anima.sp_atk * anima.stats_inc_dec["sp_atk"]
    
def _calc_def(anima: Anima, tech: Technique) -> float:
    return anima.def_ * anima.stats_inc_dec["def"] if tech.category == Category.PHYSICAL else anima.sp_def * anima.stats_inc_dec["sp_def"]

def _calc_eff(anima: Anima, tech: Technique) -> float:
    eff = 1
    
    eff *= effectiveness_chart[tech.type][anima.type_a]
    eff *= effectiveness_chart[tech.type][anima.type_b1]
    
    if getattr(anima, "type_b2", None) is not None:
        eff *= effectiveness_chart[tech.type][anima.type_b2]
    return eff