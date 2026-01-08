import os, sys
from typing import Callable, Literal, TypedDict
from functools import partial
from itertools import count

from category import Category
from anima import Anima
from secondary_effect import SecondaryEffect
from type import TypeA, TypeB

from logic.math import solve_equation, give_just_one_solution
from logic.generate.boolean import fifty_fifty

from random import randint
from dict import formula_dict
from type import effectiveness_chart
from status import Status1, Status2

_techdex_index = count(0)
'''Deberia tener una clase Techdex y esta aparte como tengo con Anima y Animadex? Muchas preguntas, pocas respuestas'''
class Technique(TypedDict): # Pensar que hacer con esto
    name: str
    power: int | None
    type: TypeA | TypeB
    category: Category
    accuracy: int | Literal["always"] # Un número o "always"
    pp: int
    secondary_effects: dict[str, int | tuple[SecondaryEffect]] | None
    priority: bool
    heal: bool
    objective: Literal["self", "one", "all", "all_enemies"]   
    battle_method: Callable # ?

    
def _techdex_entry_model(
    name: str,
    power: int | None,
    type: TypeA | TypeB,
    category: Category,
    accuracy: int | Literal["always"], # Un número o "always"
    pp: int,
    secondary_effects: SecondaryEffect | None,
    priority: bool,
    heal: bool,
    objective: Literal["self", "one", "all", "only_enemies"],
    battle_method: Callable
) -> dict[str, Technique]:
    return {
        "name": name,
        "power": power,
        "type": type,
        "category": category,
        "accuracy": accuracy,
        "pp": pp,
        "secondary_effects": secondary_effects,
        "priority": priority,
        "heal": heal,
        "objective": objective,
        "battle_method": battle_method
    }

def _secondary_effects_model(prob: int, effects: tuple[SecondaryEffect]) -> dict[str, int | tuple[SecondaryEffect]]:
    return {
        "prob": prob,
        "effects": effects
    }


def _just_damage(atack_anima: Anima, defense_Anima: Anima, tech: Technique): # Tal vez esto no vaya aqui y ni guarde metodos en el techdex who knows
    if isinstance(tech.type, TypeA):
        eff = effectiveness_chart[tech.type][defense_Anima.type_a]
    else:
        eff = effectiveness_chart[tech.type][defense_Anima.type_b1]
        if defense_Anima.type_b2 is not None:
            eff2 = effectiveness_chart[tech.type][defense_Anima.type_b2]
            eff *= eff2
    
    stab = "stab = 1.5" if tech.type in (atack_anima.type_a, atack_anima.type_b1, atack_anima.type_b2) else "stab = 1"        
    eff = f"eff = {eff}"      
    v = f"v = {randint(75, 100)}" # Me gustaria que si sale 75 ponga min damage y si sale 100 ponga max damage
    lvl = f"lvl = {atack_anima.lvl}"
    atq = f"atq = {atack_anima.atk if tech.category is Category.PHYSICAL else atack_anima.sp_atk}"
    def_ = f"def = {defense_Anima.def_ if tech.category is Category.PHYSICAL else defense_Anima.sp_def}"
    power = f"power = {tech.power}"
    
    return int(give_just_one_solution(solve_equation(formula_dict["damage"], stab, eff, v, lvl, atq, power, def_), "damage"))

def _just_damage_multiple(atack_anima: Anima, defense_Anima: Anima, tech: Technique, times: int):
    if isinstance(tech.type, TypeA):
        eff = effectiveness_chart[tech.type][defense_Anima.type_a]
    else:
        eff = effectiveness_chart[tech.type][defense_Anima.type_b1]
        if defense_Anima.type_b2 is not None:
            eff2 = effectiveness_chart[tech.type][defense_Anima.type_b2]
            eff *= eff2
    
    stab = "stab = 1.5" if tech.type in (atack_anima.type_a, atack_anima.type_b1, atack_anima.type_b2) else "stab = 1"        
    eff = f"eff = {eff}"      
    v = f"v = {randint(75, 100)}" # Me gustaria que si sale 75 ponga min damage y si sale 100 ponga max damage
    lvl = f"lvl = {atack_anima.lvl}"
    atq = f"atq = {atack_anima.atk if tech.category is Category.PHYSICAL else atack_anima.sp_atk}"
    def_ = f"def = {defense_Anima.def_ if tech.category is Category.PHYSICAL else defense_Anima.sp_def}"
    power = f"power = {tech.power}"
    
    damage = int(give_just_one_solution(solve_equation(formula_dict["damage"], stab, eff, v, lvl, atq, power, def_), "damage")) * times
    return damage


def _just_heal(anima: Anima): # Tal vez hay que poner algo mas idk
    anima.hp_now += (anima.hp_max/2)


def _just_stat_debuff(*stats: str, anima: Anima):
    """En stats importante poner solo la stat (atk, def...)"""
    
    for stat in stats:
        anima.stats_inc_dec[f"{stat}_inc_dec"] -= 1
    
def _just_stat_buff(*stats: str, anima: Anima):
    """En stats importante poner solo la stat (atk, def...)"""
    
    for stat in stats:
        anima.stats_inc_dec[f"{stat}_inc_dec"] += 1
        

def _just_protect(anima: Anima): # Esto aqui? No?
    anima.status1 = Status1.PROTECTED



def _next_techdex_key() -> str:
    return str(next(_techdex_index)).zfill(3)


techdex: dict[str, Technique] = {
    _next_techdex_key(): _techdex_entry_model("example", 10, TypeA.FLUXOR, Category.SPECIAL, 100, 10, None, False, False, "one", _just_damage), #()?
    
    _next_techdex_key(): _techdex_entry_model("Strike", 40, TypeB.COMMUNIS, Category.PHYSICAL, 100, 30, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Double Punch", 20, TypeB.COMMUNIS, Category.PHYSICAL, 90, 10, None, False, False, "one", _just_damage_multiple),
    
    _next_techdex_key(): _techdex_entry_model("Mega Punch", 80, TypeB.COMMUNIS, Category.PHYSICAL, 80, 10, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Swift", 60, TypeB.COMMUNIS, Category.SPECIAL, "always", 20, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Tri Attack", 80, TypeB.COMMUNIS, Category.SPECIAL, 100, 15, _secondary_effects_model(50, (SecondaryEffect.BURN, SecondaryEffect.PARALIZE, SecondaryEffect.FREEZE)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Restore", None, TypeB.COMMUNIS, Category.STATUS, "always", 5, None, False, True, "self", _just_heal),
    
    _next_techdex_key(): _techdex_entry_model("Leer", None, TypeB.COMMUNIS, Category.STATUS, 100, 20, None, False, False, "one", partial(_just_stat_debuff, "def")),
    
    _next_techdex_key(): _techdex_entry_model("Growl", None, TypeB.COMMUNIS, Category.STATUS, 100, 20, None, False, False, "one", partial(_just_stat_debuff, "atk")),
    
    _next_techdex_key(): _techdex_entry_model("Roar", None, TypeB.COMMUNIS, Category.STATUS, 100, 20, None, False, False, "one", partial(_just_stat_debuff, "sp_atk")),
    
    _next_techdex_key(): _techdex_entry_model("Solid armor", None, TypeB.COMMUNIS, Category.STATUS, 100, 20, None, False, False, "one", partial(_just_stat_buff, "def")),
    
    _next_techdex_key(): _techdex_entry_model("Sword Dance", None, TypeB.COMMUNIS, Category.STATUS, "always", 5, None, False, False, "self", partial(_just_stat_buff, "atk", "atk")),
    
    _next_techdex_key(): _techdex_entry_model("Fast Punch", 20, TypeB.COMMUNIS, Category.PHYSICAL, 100, 15, None, True, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Protect", None, TypeB.COMMUNIS, Category.STATUS, "always", 10, None, False, False, "self", _just_protect),
    
    _next_techdex_key(): _techdex_entry_model("Primal Flow", 120, TypeA.ESSENTIA, Category.SPECIAL, 85, 5, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Inner Ressonance", 65, TypeA.ESSENTIA, Category.SPECIAL, 100, 10, None, False, False, "only_enemies", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Being Rupture", 50, TypeA.ESSENTIA, Category.PHYSICAL, 90, 15, _secondary_effects_model(50, (SecondaryEffect.DEF_DOWN)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Essence Burst", 40, TypeA.ESSENTIA, Category.SPECIAL, 100, 30, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Essence Expansion", None, TypeA.ESSENTIA, Category.STATUS, "always", 20, None, False, False, "self", partial(_just_stat_buff, "spe", "spe")),
    
    _next_techdex_key(): _techdex_entry_model("Soul Fragment", 60, TypeA.ESSENTIA, Category.PHYSICAL, 100, 20, _secondary_effects_model(30, (SecondaryEffect.CONFUSE)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Pattern Slash", 60, TypeA.FORMA, Category.PHYSICAL, 100, 20, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Geometric Force", None, TypeA.FORMA, Category.STATUS, 100, 10, None, False, False, "only_enemies", partial(_just_stat_debuff, "spe")),
    
    _next_techdex_key(): _techdex_entry_model("Reshape", None, TypeA.FORMA, Category.STATUS, "always", 10, None, False, False, "self", partial(_just_stat_buff, "eva", "eva")),
    
    _next_techdex_key(): _techdex_entry_model("Structural Impact", 75, TypeA.FORMA, Category.PHYSICAL, 90, 10, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Adaptative Frame", 18, TypeA.FORMA, Category.SPECIAL, 90, 25, None, False, False, "one", _just_damage_multiple),
    
    _next_techdex_key(): _techdex_entry_model("Drain Mass", 75, 100, TypeA.FORMA, Category.PHYSICAL, 10, None, False, True, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Cosmic Power", 60, TypeA.FORMA, Category.SPECIAL, "always", 15, _secondary_effects_model(30, (SecondaryEffect.FLINCH)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Resolve Strike", 40, TypeA.VOLUNTAS, Category.SPECIAL, 100, 30, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Will Power", 50, TypeA.VOLUNTAS, Category.PHYSICAL, 90, 20, None, True, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("", 80, TypeA.VOLUNTAS, Category.SPECIAL, 95, 10, None, False, False, "only_enemies", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("", 120, TypeA.VOLUNTAS, Category.SPECIAL, 75, 5, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("", 60, TypeA.VOLUNTAS, Category.PHYSICAL, 95, 15, None, False, True, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("", 200, TypeA.VOLUNTAS, Category.SPECIAL, 25, 10, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Ember", 40, TypeB.IGNIS, Category.SPECIAL, 100, 30, _secondary_effects_model(15, (SecondaryEffect.BURN)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Fire Fist", 60, TypeB.IGNIS, Category.PHYSICAL, 95, 20, _secondary_effects_model(25, (SecondaryEffect.BURN)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Fire Punch", 80, TypeB.IGNIS, Category.PHYSICAL, 100, 15, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Fire Wave", 80, TypeB.IGNIS, Category.SPECIAL, 95, 15, _secondary_effects_model(15, (SecondaryEffect.BURN)), False, False, "all", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Flamethrower", 100, TypeB.IGNIS, Category.SPECIAL, 90, 10, _secondary_effects_model(30, (SecondaryEffect.BURN)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Lava Plume", 120, TypeB.IGNIS, Category.PHYSICAL, 85, 5, None, False, False, "only_enemies", _just_damage),
}
'''A dictionary of every single Technique with its information that never changes'''


tech = techdex["001"]

''' Orden movimientos en combate: 
an1 = 0
an2 = 0
mov1 = True
mov2 = True

if mov1.priority and !mov2.priority:
    pass
    #mov1()
    #mov2()
elif mov2.priority and !mov1.priority:
    pass
    #mov2()
    #mov1()
else:
    if an1.spe > an2.spe:
        pass
        #mov1()
        #mov2()
    elif an2.spe > an1.spe:
        pass
        #mov2()
        #mov1()
    else:
        if fifty_fifty():
            pass
            #mov1()
            #mov2()
        else:
            pass
            #mov2()
            #mov1()
'''
