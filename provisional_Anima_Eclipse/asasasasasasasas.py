import random
from logic.generate.boolean import fifty_fifty
from dict import effectiveness_chart

def ability1():
    pass
def ability2():
    pass

def is_weak(anima1, anima2):
    anima1_types = [anima1.type_a, anima1.type_b1, anima1.type_b2]
    anima1_types = [t for t in anima1_types if t is not None]
    
    anima2_types = [anima2.type_a, anima2.type_b1, anima2.type_b2]
    anima2_types = [t for t in anima2_types if t is not None]
    
    for t in anima2_types:
        if t in effectiveness_chart:
            for t2 in anima1_types:
                multi = effectiveness_chart[t][t2]
                if multi > 1:
                    return True
    return False


trainer1_animas = 4
trainer2_animas = 4

trainer1_option = ""

trainer2_changes = 1

anima_battling1 = "a"
anima_battling2 = "a"

while trainer1_animas != 0 and trainer2_animas != 0:
    # Inicio del turno
    # Habilidades de inicio de turno
    if anima_battling1.spe > anima_battling2.spe:
        ability1()
        ability2()
    elif anima_battling1.spe < anima_battling2.spe:
        ability2()
        ability1()
    else:
        if fifty_fifty():
            ability1()
            ability2()
        else:
            ability2()
            ability1()
            
    if trainer1_option == "fight":
        pass
    elif trainer1_option == "change":
        trainer1_change = True
    elif trainer1_option == "object":
        pass
    elif trainer1_option == "run":
        pass
    else:
        pass
            
    if is_weak(anima_battling2, anima_battling1) and trainer2_changes > 0:
        trainer2_change = True 
        trainer2_changes -= 1
    