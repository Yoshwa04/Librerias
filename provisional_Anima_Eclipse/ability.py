from dataclasses import dataclass
from typing import Literal, TypedDict

from anima import Anima
from type import TypeA, TypeB
from status import Status1

"""Esto seguramente estara muy cambiado, para empezar creo que todos los metodos de todas las habilidades deben hacer un return y no cambiar las cosas desde dentro, ya que hay habiliades como rompemoldes que necesitan recoger los cambios que se han hecho por parte de la habilidad rival. La dificultad es a la hora de hacer el loop del combate poder hacer que las habilidades hagan return y se recogan las cosas bien sin poner millones de casos posibles. Porque se debe diferenciar en cuando una habilidad te sube el ataque a ti o se lo baja al rival, no es lo mismo. 

Otra posibilidad es que haga ambas cosas. Ya que hay casos especificos de rompemoldes anulando la habilidad pero no es en todas las habilidades. Ya que aquellas que al momento de realizarse no interactuan directamente con el Anima no debe de tenerse en cuenta, la posibilidad de que si se hagan los cambios de las habilidades dentro del propio metodo pero que a parte tambien hagan un return en algun formato a verse de lo que ha hecho para que lo recoja la segunda habilidad en el orden (que podria o no ser rompemoldes) y que esta recoja esas "instrucciones" y las interprete, en ese caso todas las habilidades deben recoger una variable de instrucciones aunque solo algunas las utilicen"""  

@dataclass(slots=True)
class Ability():
    name: str
    when: Literal[
        "entering_battle", "exiting_battle",
        "start_of_turn", "end_of_turn",
        "taking_damage", "dealing_damage",
        "with_status",
        "stat_fall",
        "always",
        "foe_ability_affects_you"
    ] 
    effect: str
    '''x2/1.5... una stat - hacer daño al recibir daño fisico - absorber un tipo - recibir x2 de un tipo - recibir /2 de un tipo - Curarse si esta envenenado - atacaer un turno si otro no - 
    curarse los estados - '''
    
def ability_entry_model(
    name: str,
    when: Literal[
        "entering_battle", "exiting_battle",
        "start_of_turn", "end_of_turn",
        "taking_damage", "dealing_damage",
        "with_status",
        "stat_fall",
        "always",
        "foe_ability_affects_you"
    ], 
    effect: str
) -> Ability:
    return Ability(
        name=name,
        when=when,
        effect=effect
    )

            
abilitydex: dict[str, Ability] = {
    "000": ability_entry_model("exemple", "always", "nothing"),
    
    "001": ability_entry_model("Pure Energy", "always", "x2 atk"),
    "002": ability_entry_model("", "always", "x2 sp_atk"),
    "003": ability_entry_model("Intimidate", "entering_battle", "-1 foe atk"),
    "004": ability_entry_model("", "entering_battle", "-1 foe sp_atk"),
    "005": ability_entry_model("", "entering_battle", "-1 foe acc"),
    "006": ability_entry_model("Natural Cure", "exiting_battle", "cure status"),
    "007": ability_entry_model("NEGADOR O ALGO ASI", "stat fall", "+1 stat that fell"),
    "008": ability_entry_model("Shadow Trap", "always", "foe cant change or escape"),
    "009": ability_entry_model("Overweat", "always", "x1.5 water damage when hp/2"),
    "010": ability_entry_model("Overgrow", "always", "x1.5 plant damage when hp/2"),
    "011": ability_entry_model("Overheat", "always", "x1.5 fire damage when hp/2"),
    "012": ability_entry_model("Overcharge", "always", "x1.5 electric damage when hp/2"),
    "013": ability_entry_model("RESPONDON??????", "stat fall", "+1 atk when other stat fall"),
    "013": ability_entry_model("", "stat fall", "x2 stat changes"),
    "014": ability_entry_model("Water absorb", "taking_damage", "negates water damage and gains hp"),
    "015": ability_entry_model("Fire absorb", "taking_damage", "negates fire damage and gains hp"),
    "016": ability_entry_model("Electromotor", "taking_damage", "negates electric damage and gains hp"),
    "017": ability_entry_model("Herbivor", "taking_damage", "negates plant damage and gains hp"),
    "018": ability_entry_model("Holy Saint", "taking_damage", "negates lux damage and gains hp"),
    "019": ability_entry_model("", "taking_damage", "negates water damage and gains hp"),
}