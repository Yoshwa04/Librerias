from dataclasses import dataclass
import os, sys
from typing import Literal
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

def _next_techdex_key() -> str:
    return str(next(_techdex_index)).zfill(3)

'''Deberia tener una clase Techdex y esta aparte como tengo con Anima y Animadex? Muchas preguntas, pocas respuestas'''
@dataclass(slots=True)
class Technique(): # Pensar que hacer con esto
    name: str
    power: int | None
    type: TypeA | TypeB
    category: Category
    accuracy: int | Literal["always"] # Un número 1-100 o "always"
    pp: int
    secondary_effects: dict[int, tuple[SecondaryEffect]] | None
    priority: bool
    heal: bool
    objective: Literal["self", "one", "all", "all_enemies"]   
    battle_method: Literal[
        "damage", "damage_multiple", "damage_second_turn", "damage_recharge", "damage_go", "damage_effect", "damage_heal", "heal", "protect", "buff1", "buff2", "buff3", "debuff1", "debuff2", "debuff3", "status"
    ] # Aqui que debo hacer? -> La mayoria de ataques con sus respectivos metodos genericos cuando sean "iguales" y algunos con metodos propios dependiendo de que tan raro sea? I guess...

    
def _techdex_entry_model(
    name: str,
    power: int | None,
    type: TypeA | TypeB,
    category: Category,
    accuracy: int | Literal["always"], # Un número o "always"
    pp: int,
    secondary_effects: dict[int, tuple[SecondaryEffect]] | None,
    priority: bool,
    heal: bool,
    objective: Literal["self", "one", "all", "only_enemies"],
    battle_method: Literal["damage", "damage_multiple", "damage_second_turn", "damage_recharge", "damage_go", "damage_effect", "damage_heal", "heal", "protect", "buff1", "buff2", "buff3", "debuff1", "debuff2", "debuff3", "status"]
) -> dict[str, Technique]:
    return Technique(
        name=name,
        power=power,
        type=type,
        category=category,
        accuracy=accuracy,
        pp=pp,
        secondary_effects=secondary_effects,
        priority=priority,
        heal=heal,
        objective=objective,
        battle_method=battle_method,
    )

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


# Cambiar el metodo de callable a str
techdex: dict[str, Technique] = {
    _next_techdex_key(): _techdex_entry_model("example", 10, TypeA.FLUXOR, Category.SPECIAL, 100, 10, None, False, False, "one", _just_damage), 
    
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
    
    _next_techdex_key(): _techdex_entry_model("Protect", None, TypeB.COMMUNIS, Category.STATUS, "always", 10, None, True, False, "self", _just_protect),
    
    _next_techdex_key(): _techdex_entry_model("Regular Hit", 40, TypeA.NEUTRO, Category.PHYSICAL, 100, 30, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("", 60, TypeA.NEUTRO, Category.SPECIAL, 100, 20, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("", 90, TypeA.NEUTRO, Category.SPECIAL, 85, 10, None, False, False, "all", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("", 75, TypeA.NEUTRO, Category.PHYSICAL, 95, 15, None, True, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("", 20, TypeA.NEUTRO, Category.PHYSICAL, 95, 30, None, False, False, "one", "damage_multiple"),
    
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
    
    # Los de agua deberian tener el secondary effect? o no ya que todos mojan siempre?
    _next_techdex_key(): _techdex_entry_model("Water Gun", 40, TypeB.AQUA, Category.SPECIAL, 100, 30, _secondary_effects_model(100, (SecondaryEffect.SOAK)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Bubble", 40, TypeB.AQUA, Category.SPECIAL, 100, 30, _secondary_effects_model(100, (SecondaryEffect.SOAK)), False, False, "one", _just_damage),
     
    _next_techdex_key(): _techdex_entry_model("Water Pulse", 60, TypeB.AQUA, Category.SPECIAL, 100, 20, _secondary_effects_model(100, (SecondaryEffect.SOAK)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Heat ", 110, TypeB.AQUA, Category.SPECIAL, 85, 5, _secondary_effects_model(30, (SecondaryEffect.BURN)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Absorb", 40, TypeB.PLANTA, Category.SPECIAL, 100, 30, None, False, True, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Razor Leaf", 60, TypeB.PLANTA, Category.PHYSICAL, 100, 20, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Mega Absorb", 75, TypeB.PLANTA, Category.SPECIAL, 90, 10, None, False, True, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Petal Dance", 120, TypeB.PLANTA, Category.PHYSICAL, 80, 5, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Spore", None, TypeB.PLANTA, Category.STATUS, 100, 10, _secondary_effects_model(100, (SecondaryEffect.ASLEEP)), False, False, "one", "POR IMPLEMENTAR"),
    
    _next_techdex_key(): _techdex_entry_model("Drain Plant", None, TypeB.PLANTA, Category.STATUS, 90, 10, None, False, False, "one", "POR IMPLEMENTAR"),
    
    _next_techdex_key(): _techdex_entry_model("Paralizer", None, TypeB.PLANTA, Category.STATUS, 70, 20, _secondary_effects_model(100, (SecondaryEffect.PARALIZE)), False, False, "one", "POR IMPLEMENTAR"),
    
    _next_techdex_key(): _techdex_entry_model("Lightning", 60, TypeB.ELECTRITAS, Category.SPECIAL, 100, 20, _secondary_effects_model(30, (SecondaryEffect.PARALIZE)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Discharge", 90, TypeB.ELECTRITAS, Category.SPECIAL, 80, 10, _secondary_effects_model(20, (SecondaryEffect.PARALIZE)), False, False, "only_enemies", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Electric Punch", 90, TypeB.ELECTRITAS, Category.PHYSICAL, 90, 15, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Bolt Strike", 110, TypeB.ELECTRITAS, Category.SPECIAL, 80, 5, _secondary_effects_model(40, (SecondaryEffect.PARALIZE)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Spark shot", 75, TypeB.ELECTRITAS, Category.PHYSICAL, "always", 10, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Electric Dance", None, TypeB.ELECTRITAS, Category.STATUS, 100, 30, None, False, False, "self", _just_stat_buff),
    
    _next_techdex_key(): _techdex_entry_model("Bug Bite", 20, TypeB.INSECTUM, Category.PHYSICAL, 100, 30, _secondary_effects_model(30, (SecondaryEffect.POSION)), False, False, "one", _just_damage_multiple), #2 times
    
    _next_techdex_key(): _techdex_entry_model("XScizor", 70, TypeB.INSECTUM, Category.PHYSICAL, 95, 15, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Buzz Wave", 60, TypeB.INSECTUM, Category.SPECIAL, 95, 10, None, False, False, "only_enemies", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Rapid Horn", 40, TypeB.INSECTUM, Category.PHYSICAL, "always", 20, None, True, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Quiver Dance", None, TypeB.INSECTUM, Category.STATUS, "always", 10, None, False, False, "self", _just_stat_buff),
    
    _next_techdex_key(): _techdex_entry_model(" Song", None, TypeB.INSECTUM, Category.STATUS, 100, 20, None, False, False, "one", _just_stat_debuff),
    
    _next_techdex_key(): _techdex_entry_model("Slow String", 30, TypeB.INSECTUM, Category.SPECIAL, 100, 30, _secondary_effects_model(50, (SecondaryEffect.SPE_DOWN)), False, False, "only_enemies", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("U-Turn", 40, TypeB.INSECTUM, Category.PHYSICAL, 100, 10, None, False, False, "one", "damage_go"),
    
    _next_techdex_key(): _techdex_entry_model("Aerial Hit", 55, TypeB.VENTUS, Category.PHYSICAL, 100, 20, None,False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Fly", 90, TypeB.VENTUS, Category.PHYSICAL, 100, 10, None, False, False, "one", "DAÑO 2 TURNOS"),
    
    _next_techdex_key(): _techdex_entry_model("Wind Strike", 70, TypeB.VENTUS, Category.SPECIAL, 90, 20, None, False, False, "all", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Aeroblast", 100, TypeB.VENTUS, Category.SPECIAL, 90, 5, None, False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("CHACHARA", 60, TypeB.VENTUS, Category.PHYSICAL, 90, 10, _secondary_effects_model(50, (SecondaryEffect.CONFUSE)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Snowball", 15, TypeB.GLACIES, Category.PHYSICAL, 95, 30, _secondary_effects_model(5, (SecondaryEffect.FREEZE)), False, False, "one", _just_damage_multiple), # 2-5
    
    _next_techdex_key(): _techdex_entry_model("Ice Fang", 50, TypeB.GLACIES, Category.PHYSICAL, 100, 20, _secondary_effects_model(15, (SecondaryEffect.FREEZE)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Icicle Crush", 80, TypeB.GLACIES, Category.PHYSICAL, 85, 10, _secondary_effects_model(35, (SecondaryEffect.FLINCH)), False, False, "one", _just_damage),
    
    _next_techdex_key(): _techdex_entry_model("Ice Wind", 50, TypeB.GLACIES, Category.SPECIAL, 80, 15, None, False, False , "all", _just_damage), # Siempre es crítico
    
    _next_techdex_key(): _techdex_entry_model("Ice Burn", 140, TypeB.GLACIES, Category.SPECIAL, 90, 5, _secondary_effects_model(40, (SecondaryEffect.BURN)), False, False, "one", _just_damage), # 1 turno cargar
    
    _next_techdex_key(): _techdex_entry_model("FlashLight", 40, TypeB.LUX, Category.SPECIAL, 100, 30, _secondary_effects_model(33, (SecondaryEffect.BLIND)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Sacred Fire", 60, TypeB.LUX, Category.SPECIAL, 95, 20, _secondary_effects_model(20, (SecondaryEffect.BURN)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Divine Punch", 75, TypeB.LUX, Category.PHYSICAL, 100, 15, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Angel Aura", 80, TypeB.LUX, Category.SPECIAL, 85, 10, None, False, False, "only_enemies", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("God's Word", None, TypeB.LUX, Category.STATUS, "always", 5, None, False, True, "self", "heal"),
    
    _next_techdex_key(): _techdex_entry_model("Saint Strike", 140, TypeB.LUX, Category.PHYSICAL, 80, 5, None, False, False, "one", "damage_recharge"),
    
    _next_techdex_key(): _techdex_entry_model("Dark Pulse", 40, TypeB.SINISTER, Category.SPECIAL, 100, 20, None, False, False, "only_enemies", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Pursuit", 40, TypeB.SINISTER, Category.PHYSICAL, "always", 10, None, False, False, "one", "damage_effect"), #?
    
    _next_techdex_key(): _techdex_entry_model("Crunch", 80, TypeB.SINISTER, Category.PHYSICAL, 100, 15, _secondary_effects_model(50, (SecondaryEffect.DEF_DOWN)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Night Slash", 70, TypeB.SINISTER, Category.PHYSICAL, 100, 15, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Scary Face", None, TypeB.SINISTER, Category.STATUS, 100, 25, None, False, False, "only_enemies", "status"),
    
    _next_techdex_key(): _techdex_entry_model("Shadow Ball", 60, TypeB.PHANTASMA, Category.SPECIAL, 100, 20, _secondary_effects_model(40, (SecondaryEffect.SDEF_DOWN)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Sneaky Punch", 75, TypeB.PHANTASMA, Category.PHYSICAL, 95, 15, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Nightmare Rush", 90, TypeB.PHANTASMA, Category.PHYSICAL, 100, 10, None, False, False, "one", "damage_second_turn"),
    
    _next_techdex_key(): _techdex_entry_model("Death Beam", 120, TypeB.PHANTASMA, Category.SPECIAL, 80, 5, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Dream Eater", 75, TypeB.PHANTASMA, Category.SPECIAL, 90, 10, None, False, True, "one", "damage_heal"),
    
    _next_techdex_key(): _techdex_entry_model("Horror Tale", None, TypeB.PHANTASMA, Category.STATUS, "always", 10, None, False, False, "one", "status"),
    
    _next_techdex_key(): _techdex_entry_model("Fake Slam", 35, TypeB.PHANTASMA, Category.PHYSICAL, 100, 25, None, False, False, "one", "damage_multiple"),
    
    _next_techdex_key(): _techdex_entry_model("Psyquic", 60, TypeB.PSYCHICUS, Category.SPECIAL, 100, 20, _secondary_effects_model(25, (SecondaryEffect.CONFUSE)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Kinetic", 30, TypeB.PSYCHICUS, Category.PHYSICAL, "always", 25, None, True, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Confussion", 90, TypeB.PSYCHICUS, Category.SPECIAL, 90, 10, _secondary_effects_model(50, (SecondaryEffect.CONFUSE)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Mind Reading", None, TypeB.PSYCHICUS, Category.STATUS, "always", 10, None, False, False, "one", "debuff2"),
    
    _next_techdex_key(): _techdex_entry_model("Psique Wave", 100, TypeB.PSYCHICUS, Category.PHYSICAL, 85, 5, None, False, False, "all", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Power Punch", 40, TypeB.PUGNA, Category.PHYSICAL, 100, 30, _secondary_effects_model(100, (SecondaryEffect.ATK_UP)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Low Kick", 50, TypeB.PUGNA, Category.PHYSICAL, 100, 15, None, True, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("High Jump Kick", 100, TypeB.PUGNA, Category.PHYSICAL, 90, 10, None, False, False, "one", "damage"), # Esta es el que si fallas te haces daño
    
    _next_techdex_key(): _techdex_entry_model("Drain Punch", 75, TypeB.PUGNA, Category.PHYSICAL, 90, 10, None, False, True, "one", "damage_heal"),
    
    _next_techdex_key(): _techdex_entry_model("Demolition", 60, TypeB.PUGNA, Category.SPECIAL, "always", 20, None, False, False, "only_enemies", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Focus", None, TypeB.PUGNA, Category.STATUS, "always", 20, None, False, False, "self", "buff1"),
    
    _next_techdex_key(): _techdex_entry_model("Bullet Punch", 40, TypeB.METALLUM, Category.PHYSICAL, "always", 20, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Heavy Body", 80, TypeB.METALLUM, Category.PHYSICAL, 95, 10, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Iron Headbutt", 75, TypeB.METALLUM, Category.PHYSICAL, 100, 15, _secondary_effects_model(30, (SecondaryEffect.CONFUSE)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Iodo", 60, TypeB.METALLUM, Category.SPECIAL, 100, 20, None, False, False, "all", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("", 120, TypeB.METALLUM, Category.PHYSICAL, 80, 5, _secondary_effects_model(30, (SecondaryEffect.FLINCH)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("", 90, TypeB.METALLUM, Category.SPECIAL, 90, 10, _secondary_effects_model(50, (SecondaryEffect.BLIND)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Heavy Armor", None, TypeB.METALLUM, Category.STATUS, "always", 20, None, False, False, "self", "buff2"),
    
    _next_techdex_key(): _techdex_entry_model("Rubbish Punch", 75, TypeB.VENENUM, Category.PHYSICAL, 100, 15, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Poison Fang", 60, TypeB.VENENUM, Category.PHYSICAL, 100, 20, _secondary_effects_model(40, (SecondaryEffect.POSION)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("", 60, TypeB.VENENUM, Category.SPECIAL, 90, 20, _secondary_effects_model(30, (SecondaryEffect.POSION)), False, False, "only_enemies", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("", 40, TypeB.VENENUM, Category.SPECIAL, 100, 30, _secondary_effects_model(20, (SecondaryEffect.POSION)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("", 120, TypeB.VENENUM, Category.SPECIAL, 85, 5, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("", 150, TypeB.VENENUM, Category.PHYSICAL, 85, 5, _secondary_effects_model(50, (SecondaryEffect.POSION)), False, False, "one", "damage_recharge"),
    
    _next_techdex_key(): _techdex_entry_model("Rock Slide", 45, TypeB.RUPES, Category.PHYSICAL, 100, 25, None, False, False, "only_enemies", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Power Gem", 100, TypeB.RUPES, Category.SPECIAL, 85, 5, _secondary_effects_model(50, (SecondaryEffect.SATK_UP)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("Anti Aerial", 50, TypeB.RUPES, Category.PHYSICAL, 100, 20, _secondary_effects_model(100, (SecondaryEffect.CONFUSE)), False, False, "one", "damage"), # El efecto debe ser solo a tipo volador
    
    _next_techdex_key(): _techdex_entry_model("Rock Throw", 70, TypeB.RUPES, Category.PHYSICAL, "always", 10, None, False, False, "one", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Earthquake", 90, TypeB.TERRA, Category.PHYSICAL, 95, 10, None, False, False, "all", "damage"),
    
    _next_techdex_key(): _techdex_entry_model("Sand ", 55, TypeB.TERRA, Category.SPECIAL, 100, 15, _secondary_effects_model(50, (SecondaryEffect.BLIND)), False, False, "one", "damage_effect"),
    
    _next_techdex_key(): _techdex_entry_model("One Thousand Arrows", 95, TypeB.TERRA, Category.SPECIAL, 90, 10, None, False, False, "only_enemies", "damage"), # Este tambien da a voladores
    
    _next_techdex_key(): _techdex_entry_model("Dig", 75, TypeB.TERRA, Category.PHYSICAL, 100, 15, None, False, False, "one", "damage_second_turn"),
    
    _next_techdex_key(): _techdex_entry_model("", None, TypeB.TERRA, Category.STATUS, 100, 20, None, False, False, "one", "debuff1"),
    
    _next_techdex_key(): _techdex_entry_model(),
}
'''A dictionary of every single Technique with its information.'''


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
