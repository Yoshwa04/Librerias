from enum import Enum

'''
    Deberia cambiarlo y hacer algo tipo:
    - Status1 -> Vivo/Debilitado
    - Status2 -> Nada, Quemado, veneno... (estados alterados de ese tipo)
    - Status3 -> Nada, Confuso, enamorado... (estados alterados de ese tipo)
    - Status4 -> Nada, protegido, oculto
    
    Ya que puede estar vivo y a la vez quemado y confuso
    
    Los llamo de alguna manera diferente en vez de 1, 2, 3...??
    
    Status1 -> AliveStatus
    Status2 -> ElementStatus
    Status3 -> BehaveStatus
    Status4 -> SpecialStatus
    '''

class AliveStatus(Enum):
    ALIVE = "Alive"
    FAINTED = "Fainted"
    
    
class ElementStatus(Enum):
    NOTHING = "Nothing"
    BURNED = "Burned"
    PARALIZED = "Paralized"
    POISONED = "Poisoned"
    FROZEN = "Frozen"
    WET = "Wet"
    ASLPEEP = "Asleep"
    
class BehaveStatus(Enum):
    NOTHING = "Nothing"
    CONFUSED = "Confused"
    ANGRY = "Angry"
    ENAMORED = "Enamored"
    BLINDED = "Blinded"
    FLINCHED = "Flinched" # can't atack 1 turn
    
class SpecialStatus(Enum):
    NOTHING = "Nothing"
    HIDDEN = "Hidden" # fly, dig... 0 damage with exceptions
    PROTECTED = "Protected" # 0 damage & status