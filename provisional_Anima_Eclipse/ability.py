from typing import Callable, TypedDict

from anima import Anima
from status import Status1

class Ability(TypedDict):
    name: str
    effect: Callable[[Anima], int]
    
    
abilitydex: dict[str, Ability] = {
    "000": {
        "name": "example",
        "effect": lambda anima: setattr(anima, 'atk', anima.atk * 2)
    },
    "0000": {
        "name": "example2",
        "effect": lambda anima: setattr(anima, 'status1', Status1.BURNED)
    }
}