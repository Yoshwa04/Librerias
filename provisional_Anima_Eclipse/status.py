from enum import Enum


class Status1(Enum):
    GOOD = "Good"
    INVULNERABLE = "Invulnerable" # no status1 damage
    HIIDEN = "Hidden" # fly, dig... 0 damage with excepcions
    FAINTED = "Fainted"
    BURNED = "Burned"
    PARALIZED = "Paralized"
    POISONED = "Poisoned"
    FROZEN = "Frozen"
    WET = "Wet"
    ASLPEEP = "Asleep"
    PROTECTED = "Protected" # 0 damage & status
    
    
class Status2(Enum):
    GOOD = "Good"
    INVULNERABLE = "Invulnerable" # no status2 damage 
    CONFUSED = "Confused"
    ANGRY = "Angry"
    ENAMORED = "Enamored"
    BLINDED = "Blinded"
    FLINCHED = "Flinched" # can't atack