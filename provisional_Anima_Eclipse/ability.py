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
        "try to run/change", "foe tries to change",
        "with_status",
        "stat_fall",
        "always",
        "foe_ability_affects_you"
    ] 
    effect: str
    '''x2/1.5... una stat - hacer daño al recibir daño fisico - absorber un tipo - recibir x2 de un tipo - recibir /2 de un tipo - Curarse si esta envenenado - atacar un turno si otro no - 
    curarse los estados - '''
    
def ability_entry_model(
    name: str,
    when: Literal[
        "entering_battle", "exiting_battle",
        "start_of_turn", "end_of_turn",
        "taking_damage", "dealing_damage",
        "try to run/change", "foe tries to change",
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
    
    "001": ability_entry_model("Huge Power", "always", "x2 atk"),
    "002": ability_entry_model("Canalize", "always", "x2 sp_atk"),
    "003": ability_entry_model("Intimidate", "entering_battle", "-1 foe atk"),
    "004": ability_entry_model("Disrupt", "entering_battle", "-1 foe sp_atk"),
    "005": ability_entry_model("Flash", "entering_battle", "-1 foe acc"),
    "006": ability_entry_model("Natural Cure", "exiting_battle", "cure status"),
    "007": ability_entry_model("Contrary", "stat fall", "Inverts stat changes (+1 is now -1...)"),
    "008": ability_entry_model("Shadow Trap", "foe tries to change", "foe cant change or escape"),
    "009": ability_entry_model("Overweat", "dealing_damage", "x1.5 water damage when hp/2"),
    "010": ability_entry_model("Overgrow", "dealing_damage", "x1.5 plant damage when hp/2"),
    "011": ability_entry_model("Overheat", "dealing_damage", "x1.5 fire damage when hp/2"),
    "012": ability_entry_model("Overcharge", "dealing_damage", "x1.5 electric damage when hp/2"),
    "013": ability_entry_model("RESPONDON??????", "stat fall", "+1 atk when other stat fall"),
    "013": ability_entry_model("Simple", "stat fall", "x2 stat changes"),
    "014": ability_entry_model("Water absorb", "taking_damage", "negates water damage and gains hp"),
    "015": ability_entry_model("Fire absorb", "taking_damage", "negates fire damage and gains hp"),
    "016": ability_entry_model("Electromotor", "taking_damage", "negates electric damage and gains hp"),
    "017": ability_entry_model("Herbivor", "taking_damage", "negates plant damage and gains hp"),
    "018": ability_entry_model("Holy Saint", "taking_damage", "negates lux damage and gains hp"),
    "019": ability_entry_model("Antidote", "with_status", "heals if poisoned instead of losing hp"),
    "020": ability_entry_model("Absent?", "dealing_damage", "needs to rest 1 turn after atacking"),
    "021": ability_entry_model("Joker", "always", "status atacks have priority"),
    "022": ability_entry_model("Fluffy", "taking_damage", "takes x2 fire damage, but /2 physical damage"),
    "023": ability_entry_model("Speed Boost", "end_of_turn", "+1 speed at the end"),
    "024": ability_entry_model("Battle Armor"),
    "025": ability_entry_model("Sturdy", "taking_damage", "resists one hit ko with 1 hp"),
    "026": ability_entry_model("Compound eyes", ),
    "027": ability_entry_model("Shield Dust", "taking_damage", "Prevents status atacks"),
    "028": ability_entry_model("Rough Skin", "taking_damage", "deals damage when taking physical damage"),
    "029": ability_entry_model("Effect Spore", "taking_damage", "paralizes, sleeps or poisons when taking damage (33%)"),
    "030": ability_entry_model("Synchronize", "always", "passes the status change to the foe that gave it"),
    "031": ability_entry_model("Serene Grace (DICHA)", "dealing_damage", "augments the secondary effect chance"),
    "032": ability_entry_model("Trace"),
    "033": ability_entry_model("Toxic Point", "taking_damage", "poisons when taking physical damage"),
    "034": ability_entry_model("Thick Fat", "taking_damage", "takes /2 damage from fire and ice"),
    "035": ability_entry_model("Early Bird", "always", "wakes up faster when asleep"),
    "036": ability_entry_model("Flame Body", "taking_damage", "burns when taking physical damage"),
    "037": ability_entry_model("Run Away", "always", "runs away always from wild animas"),
    "038": ability_entry_model("Hustle"),
    "039": ability_entry_model("Swarm"),
    "040": ability_entry_model("Rock Head", "dealing_damage", "does not take recoil damage"),
    "041": ability_entry_model("Anger Point", "taking_damage", "+1 atk and sp atk when taking a x2"),
    "042": ability_entry_model("Levitate", "always", "avoids ground atacks"),
    "043": ability_entry_model("Mold Breaker", "foe_ability_affects_you", "negates the effects of the foe ability affecting you or your atacks"),
    "044": ability_entry_model("Insomnia", "always", "prevents from falling asleep"),
    "045": ability_entry_model("Veleta", "end_of_turn", "+2 one random stat, -1 another random stat"),
    "046": ability_entry_model("Slow Start", "entering_battle", "/2 atk and def the 2 first turns"),
    "047": ability_entry_model("Compensation", "taking_damage", "/2 damage when hp=100%"),
    "048": ability_entry_model("Wonder Guard", "taking_damage", "Only x2 attacks affects on him"),
    "049": ability_entry_model("True Neutral", "dealing_damage", "x2 attacks are now x1, but x0.5 are x1 too"),
    "050": ability_entry_model("Low Guard", "taking_damage", "-1 def and sp def when taking a x2"),
    "051": ability_entry_model("Calc", "entering_battle", "copies the stat changes of your foe (good and bad ones)"),
    "052": ability_entry_model("Lynx", "dealing_damage", "+1 critical index"),
    "053": ability_entry_model("Typycalize", "always", "converts neutral attacks in your TypeA & communis in your TypeB (if 2 TypeB, takes the primal)"),
    
}