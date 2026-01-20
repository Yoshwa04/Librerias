from typing import Callable, Literal, TypedDict

from anima import Anima
from type import TypeA, TypeB
from status import Status1

"""Esto seguramente estara muy cambiado, para empezar creo que todos los metodos de todas las habilidades deben hacer un return y no cambiar las cosas desde dentro, ya que hay habiliades como rompemoldes que necesitan recoger los cambios que se han hecho por parte de la habilidad rival. La dificultad es a la hora de hacer el loop del combate poder hacer que las habilidades hagan return y se recogan las cosas bien sin poner millones de casos posibles. Porque se debe diferenciar en cuando una habilidad te sube el ataque a ti o se lo baja al rival, no es lo mismo. 

Otra posibilidad es que haga ambas cosas. Ya que hay casos especificos de rompemoldes anulando la habilidad pero no es en todas las habilidades. Ya que aquellas que al momento de realizarse no interactuan directamente con el Anima no debe de tenerse en cuenta, la posibilidad de que si se hagan los cambios de las habilidades dentro del propio metodo pero que a parte tambien hagan un return en algun formato a verse de lo que ha hecho para que lo recoja la segunda habilidad en el orden (que podria o no ser rompemoldes) y que esta recoja esas "instrucciones" y las interprete, en ese caso todas las habilidades deben recoger una variable de instrucciones aunque solo algunas las utilicen"""  

class Ability(TypedDict):
    name: str
    when: Literal["entering_battle", "exiting_battle", 
                  "start_of_turn", "end_of_turn", 
                  "taking_damage", "dealing_damage", 
                  "with_status", 
                  "stat_fall", 
                  "always", 
                  "foe_ability_affects_you"] 
    effect: str
    '''x2 una stat - hacer daño al recibir daño fisico - absorber un tipo - recibir x2 de un tipo - recibir /2 de un tipo - Curarse si esta envenenado - atacaer un turno si otro no - 
    curarse los estados - '''
                
abilitydex: dict[str, Ability] = {
    "000": {
        "name": "example",
        "when": "entering_battle",
        "effect": "nothing"
    },
    "001": {
        
    }
}