from typing import Optional
def metodo():
    anima_yo_atq = 1
    
    anima_yo_atq += 0.25
    print("Rompemoldes evita habilidad1 rival")

posibilidades = {
    "ATAQUE BAJADO": metodo,
    "aaa": "metodo"
}



def habiliad1():
    anima_rival_atq = 1
    
    anima_rival_atq -= 0.25   
    print("Ataque del rival bajado") 
    return "ATAQUE BAJADO"

def rompemoldes(instrucciones: Optional[str] = None):
    accion = posibilidades[instrucciones]
    
    accion()
    
    
retorno = habiliad1()
rompemoldes(retorno)

    
    
    
    