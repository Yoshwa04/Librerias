from typing import Callable, TypedDict

from anima import Anima
from type import TypeA, TypeB
from status import Status1

"""Esto seguramente estara muy cambiado, para empezar creo que todos los metodos de todas las habilidades deben hacer un return y no cambiar las cosas desde dentro, ya que hay habiliades como rompemoldes que necesitan recoger los cambios que se han hecho por parte de la habilidad rival. La dificultad es a la hora de hacer el loop del combate poder hacer que las habilidades hagan return y se recogan las cosas bien sin poner millones de casos posibles. Porque se debe diferenciar en cuando una habilidad te sube el ataque a ti o se lo baja al rival, no es lo mismo. 

Otra posibilidad es que haga ambas cosas. Ya que hay casos especificos de rompemoldes anulando la habilidad pero no es en todas las habilidades. Ya que aquellas que al momento de realizarse no interactuan directamente con el Anima no debe de tenerse en cuenta, la posibilidad de que si se hagan los cambios de las habilidades dentro del propio metodo pero que a parte tambien hagan un return en algun formato a verse de lo que ha hecho para que lo recoja la segunda habilidad en el orden (que podria o no ser rompemoldes) y que esta recoja esas "instrucciones" y las interprete, en ese caso todas las habilidades deben recoger una variable de instrucciones aunque solo algunas las utilicen"""  
class Ability(TypedDict):
    name: str
    effect: Callable[[Anima], int]
    
    
  
    
def stat_boost_ability(anima: Anima, stat_name: str, multiplier: float):
    if anima.ability_uses >= 1:
        return 0
    
    anima.ability_uses += 1
    
    current = getattr(anima, stat_name)
    setattr(anima, stat_name, current * multiplier)
    
    return 1
        
def potentiate_technique_power_ability(anima: Anima):
    if anima.ability_uses >= 1:
        return 0
    if anima.hp_now > anima.hp_max * 0.5:
        return 0
    
    anima.ability_uses += 1
    
    for tech in anima.technique_set.items():
        
        if tech["type"] in (anima.type_a, anima.type_b) and tech["power"] is not None:
            tech["power"] *= 1.5
            
    return 1

def status_techniques_priority(anima: Anima):
    if anima.ability_uses >= 1:
        return 0
    
    anima.ability_uses += 1
    
    for tech in anima.technique_set.items():
        if tech["category"] == "status":
            tech["priority"] = True
            
    return 1
            
def more_resistance_less_def(anima: Anima, type: TypeB | TypeA): 
    if anima.ability_uses == 0:
        anima.def_ *= 0.8
    
    # terminar
    
    anima.ability_uses += 1
    return 1

def decrease_stat_beginning(p_anima: Anima, ai_anima: Anima, stat: str):
    if p_anima.ability_uses == 0:
        setattr(ai_anima, stat, getattr(ai_anima, stat) - 0.25)
    else:
        return 0    
    return 1
                
abilitydex: dict[str, Ability] = {
    "000": {
        "name": "example",
        "effect": lambda anima: setattr(anima, 'atk', anima.atk * 2)
    },
    "0000": {
        "name": "example2",
        "effect": lambda anima: setattr(anima, 'status1', Status1.BURNED)
    },
    
    "001": {
        "name": "Physical Rock",
        "effect": lambda anima: stat_boost_ability(anima, "atk", 1.2)
    },
    "002": {
        "name": "Highly Gifted",
        "effect": lambda anima: stat_boost_ability(anima, "sp_atk", 1.2)
    },
    "003": {
        "name": "Wall",
        "effect": lambda anima: stat_boost_ability(anima, "def_", 1.2)
    },
    "004": {
        "name": "Magnetic Force",
        "effect": lambda anima: stat_boost_ability(anima, "sp_def", 1.2)
    },
    "005": {
        "name": "Torrent",
        "effect": potentiate_technique_power_ability
    },
    "006": {
        "name": "Blaze",
        "effect": potentiate_technique_power_ability
    },
    "007": {
        "name": "Overgrow",
        "effect": potentiate_technique_power_ability
    }
}



