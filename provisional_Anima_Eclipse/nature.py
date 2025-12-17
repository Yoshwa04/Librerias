from enum import Enum

from constants import DECREASE, INCREASE

class Nature(Enum):
    BERSERKER = "Berserker"
    GLADIADOR = "Gladiador"
    ASALTANTE = "Asaltante"
    BRUTO = "Bruto"
    
    GUARDIA = "Guardia"
    MURALLA = "Muralla"
    CENTINELA = "Centinela"
    FORTIFICADO = "Fortificado"
    
    HECHICERO = "Hechicero"
    ORACULO = "Óraculo"
    MISTICO = "Místico"
    ERUDITO = "Erudito"
    
    MONJE = "Monje"
    ILUMINADO = "Iluminado"
    ADIVINO = "Adivino"
    ESPIRITUAL = "Espiritual"
    
    EXPLORADOR = "Explorador"
    CAZADOR = "Cazador"
    BROMISTA = "Bromista"
    ESPADACHIN = "Espadachín"
    
    NEUTRA = "Neutra"
    

nature_dict: dict[Nature, dict[str, str | None]] = {
    Nature.BERSERKER:   {INCREASE: "atk", DECREASE: "def"},
    Nature.GLADIADOR:   {INCREASE: "atk", DECREASE: "sp_def"},
    Nature.ASALTANTE:   {INCREASE: "atk", DECREASE: "spe"},
    Nature.BRUTO:       {INCREASE: "atk", DECREASE: "sp_atk"},  
    
    Nature.GUARDIA:     {INCREASE: "def", DECREASE: "atk"},
    Nature.MURALLA:     {INCREASE: "def", DECREASE: "sp_atk"},
    Nature.CENTINELA:   {INCREASE: "def", DECREASE: "sp_def"},
    Nature.FORTIFICADO: {INCREASE: "def", DECREASE: "spe"},
    
    Nature.HECHICERO:   {INCREASE: "sp_atk", DECREASE: "atk"},
    Nature.ORACULO:     {INCREASE: "sp_atk", DECREASE: "def"},
    Nature.MISTICO:     {INCREASE: "sp_atk", DECREASE: "sp_def"},
    Nature.ERUDITO:     {INCREASE: "sp_atk", DECREASE: "spe"},
    
    Nature.MONJE:       {INCREASE: "sp_def", DECREASE: "atk"},
    Nature.ILUMINADO:   {INCREASE: "sp_def", DECREASE: "sp_atk"},
    Nature.ADIVINO:     {INCREASE: "sp_def", DECREASE: "def"},
    Nature.ESPIRITUAL:  {INCREASE: "sp_def", DECREASE: "spe"},  
    
    Nature.EXPLORADOR:  {INCREASE: "spe", DECREASE: "def"},
    Nature.CAZADOR:     {INCREASE: "spe", DECREASE: "sp_def"},
    Nature.BROMISTA:    {INCREASE: "spe", DECREASE: "atk"},
    Nature.ESPADACHIN:  {INCREASE: "spe", DECREASE: "sp_atk"},
    
    Nature.NEUTRA:      {INCREASE: None, DECREASE: None},
}
'''The dictionary of which stats increase or decrease for each nature'''