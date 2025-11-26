from enum import Enum

class SecondaryEffect(Enum):
    BURN = "Burn"
    PARALIZE = "Paralize"
    FREEZE = "Freeze"
    POSION = "Poison"
    SOAK = "Soak"
    ASLEEP = "Asleep"
    FAINT = "Faint"
    
    CONFUSE = "Confuse"
    ANNOY = "Annoy"
    CHARM = "Charm"
    BLIND = "Blind"
    FLINCH = "Flinch"
    
    ATK_UP = "Attack up"
    ATK_DOWN = "Attack down"
    
    SATK_UP = "Special attack up"
    SATK_DOWN = "Special attack down"
    
    DEF_UP = "Defense up"
    DEF_DOWN = "Defense down"
    
    SDEF_UP = "Special defense up"
    SDEF_DOWN = "Special defense down"
    
    SPE_UP = "Speed up"
    SPE_DOWN = "Speed down"
    
    ACC_UP = "Accuracy up"
    ACC_DOWN = "Accuracy down"
    
    EVA_UP = "Evasion up"
    EVA_DOWN = "Evasion down"
    
    