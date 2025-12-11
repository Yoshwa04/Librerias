import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collections import defaultdict
from typing import Dict
from arcana import Arcana
from technique import techdex
from type import TypeA, TypeB
from nature import Nature
from ability import Ability, abilitydex
from constants import INCREASE, DECREASE


def animadex_base_stats_model(hp: int, atk: int, sp_atk: int, _def: int, sp_def: int, spe: int) -> Dict[str, int]:
    '''This method just returns a dict of the stats given its value'''
    return {
        "hp" : hp,
        "atk" : atk,
        "sp_atk" : sp_atk,
        "def" : _def,
        "sp_def" : sp_def,
        "spe" : spe,  
    }

def animadex_abilitys_model(ability1: str, ability2: str, hidden: str) -> Dict[str, Ability]:
    '''This method just returns a dict of the abilitys given'''
    return {
        "001" : ability1,
        "002" : ability2,
        "00H" : hidden,  
    }


growth_dict = {
    "fast": "growth = 4 * lvl**3 / 5",
    "normal": "growth = lvl**3",
    "slow": "growth = 5 * lvl**3 / 4",
    "parabolic": "growth = 6 * lvl**3 / 5 - 15 * lvl**2 + 100 * lvl -140",
}
'''Possible growth forms for the Animas'''

formula_dict = {
    "hp": "hp = (lvl/100 * ((stat_base*2) + potential)) + lvl",
    "stat": "stat = (5 + (lvl/100 * ((stat_base*2) + potential))) * nature",
    "catch": "catch = (hp_max*3 - hp_now*2) * catch_ratio * ball_ratio/hp_max*3 * status",
    "damage": f"damage = 1/100 * stab * eff * v * ((2/10 * lvl + 1) * atq * power/25 * def + 2)",
    "exp_given": "exp_given = (exp_base_given*lvl/participants/5) * ((2*lvl+10)**(5/2)) / ((lvl+ally_lvl+10)**(5/2)) + 1) * combat_type * object_mod * arcana_mod", 
                 # combat_type: si es wild 1 si no 1.5
    "growth": growth_dict,
    "hit_chance": "hit_chance = move_accuracy * (attacker_accuracy/defender_evasion)", 
                  # Este número sera el que se use cuando se verifique en combate, con uno random del 1 al 100, si es mayor o igual a ese random entonces le da
}
'''A bunch of formulas'''

nature_dict = {
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

effectiveness_chart = {
    TypeA.ESSENTIA:     defaultdict(lambda: 1,{TypeA.UMBRA: 2, TypeA.FORMA: 0.5,}),
    TypeA.FORMA:        defaultdict(lambda: 1,{TypeA.UMBRA: 0.5, TypeA.ESSENTIA: 2,}),
    TypeA.UMBRA:        defaultdict(lambda: 1,{TypeA.FORMA: 2, TypeA.ESSENTIA: 0.5,}),
    
    TypeB.IGNIS:        defaultdict(lambda: 1,{
        TypeB.PLANTA: 2, TypeB.GLACIES: 2, TypeB.INSECTUM: 2, TypeB.METALLUM: 2,
        TypeB.RUPES: 0.5, TypeB.TERRA: 0.5, TypeB.AQUA: 0.5, TypeB.IGNIS: 0.5
        }),
    TypeB.AQUA:         defaultdict(lambda: 1,{
        TypeB.IGNIS: 2, TypeB.TERRA: 2, TypeB.RUPES: 2,
        TypeB.PLANTA: 0.5, TypeB.METALLUM: 0.5, TypeB.AQUA:0.5
        }),
    TypeB.PLANTA:       defaultdict(lambda: 1,{
        TypeB.AQUA: 2, TypeB.TERRA: 2, TypeB.RUPES: 2,
        TypeB.IGNIS: 0.5, TypeB.METALLUM: 0.5, TypeB.INSECTUM: 0.5, TypeB.PLANTA: 0.5, TypeB.VENENUM: 0.5
        }),
    TypeB.ELECTRITAS:   defaultdict(lambda: 1,{
        TypeB.AQUA: 2, TypeB.VENTUS: 2,
        TypeB.RUPES: 0.5, TypeB.ELECTRITAS: 0.5, TypeB.PLANTA: 0.5,
        TypeB.TERRA: 0
        }),
    TypeB.INSECTUM:     defaultdict(lambda: 1,{
        TypeB.PLANTA: 2, TypeB.SINISTER: 2, TypeB.PSYCHICUS: 2,
        TypeB.IGNIS: 0.5, TypeB.METALLUM: 0.5, TypeB.VENTUS: 0.5, TypeB.RUPES: 0.5, TypeB.PUGNA: 0.5
        }),
    TypeB.VENTUS:       defaultdict(lambda: 1,{
        TypeB.PLANTA: 2, TypeB.INSECTUM: 2, TypeB.PUGNA: 2,
        TypeB.RUPES: 0.5, TypeB.METALLUM: 0.5, TypeB.ELECTRITAS: 0.5
        }),
    TypeB.GLACIES:      defaultdict(lambda: 1,{
        TypeB.VENTUS: 2, TypeB.INSECTUM: 2, TypeB.PLANTA: 2, TypeB.TERRA: 2,
        TypeB.RUPES: 0.5, TypeB.METALLUM: 0.5, TypeB.GLACIES: 0.5
        }),
    TypeB.VENENUM:      defaultdict(lambda: 1,{
        TypeB.PLANTA: 2, TypeB.LUX: 2,
        TypeB.VENENUM: 0.5, TypeB.TERRA: 0.5, TypeB.RUPES: 0.5,
        TypeB.METALLUM: 0
        }),
    TypeB.RUPES:        defaultdict(lambda: 1,{
        TypeB.GLACIES: 2, TypeB.VENTUS: 2, TypeB.INSECTUM: 2, TypeB.IGNIS: 2,
        TypeB.TERRA: 0.5, TypeB.METALLUM: 0.5, TypeB.PUGNA: 0.5, TypeB.AQUA: 0.5
        }),
    TypeB.TERRA:        defaultdict(lambda: 1,{
        TypeB.IGNIS: 2, TypeB.VENENUM: 2, TypeB.RUPES: 2, TypeB.METALLUM: 2, TypeB.ELECTRITAS: 2,
        TypeB.INSECTUM: 0.5, TypeB.PLANTA: 0.5,
        TypeB.VENTUS: 0
        }),
    TypeB.LUX:          defaultdict(lambda: 1,{
        TypeB.SINISTER: 2, TypeB.PUGNA: 2,
        TypeB.VENENUM: 0.5
        }),
    TypeB.SINISTER:     defaultdict(lambda: 1,{
        TypeB.LUX: 2, TypeB.PHANTASMA: 2,
        TypeB.PSYCHICUS: 0.5
        }),
    TypeB.PHANTASMA:    defaultdict(lambda: 1,{
        TypeB.PSYCHICUS: 2, TypeB.PHANTASMA: 2,
        TypeB.SINISTER: 0.5,
        TypeB.PUGNA: 0
        }),
    TypeB.PSYCHICUS:    defaultdict(lambda: 1,{
        TypeB.VENENUM: 2, TypeB.PUGNA: 2,
        TypeB.METALLUM: 0.5, TypeB.PSYCHICUS: 0.5,
        TypeB.SINISTER: 0
        }),
    TypeB.PUGNA:        defaultdict(lambda: 1,{
        TypeB.METALLUM: 2, TypeB.RUPES: 2, TypeB.GLACIES: 2, TypeB.SINISTER: 2,
        TypeB.INSECTUM: 0.5, TypeB.LUX: 0.5, TypeB.PSYCHICUS: 0.5, TypeB.VENTUS: 0.5, TypeB.VENENUM: 0.5,
        TypeB.PHANTASMA: 0
        }),
    TypeB.METALLUM:     defaultdict(lambda: 1,{
        TypeB.GLACIES: 2, TypeB.RUPES: 2,
        TypeB.METALLUM: 0.5, TypeB.AQUA: 0.5, TypeB.ELECTRITAS: 0.5, TypeB.IGNIS: 0.5
        }),
}
'''A dictionary that contains the effectiveness of each type against others'''

stat_increases_decreases_dict = {
    -6: 2/8,
    -5: 2/7,
    -4: 2/6,
    -3: 2/5,
    -2: 2/4,
    -1: 2/3,
    0: 2/2,
    1: 3/2,
    2: 4/2,
    3: 5/2,
    4: 6/2,
    5: 7/2,
    6: 8/2,
}
'''A dictionary that contains the min and max increases/decreases a regular stat can have (atk, sp atk, def, sp def, spe)'''

critical_index_dict = {   
    0: 6.25,
    1: 12.5,
    2: 25,
    3: 33.3,
    4: 50,
    5: 75,
    6: 100
}
'''A dictionary that contains the critical hit chance percentages based on the index'''


animadex = { 
    "000": { #Ejemplo
        "name": "a",    
        "types": [TypeA.NEUTRO, TypeB.NEUTRO],
        "abilities": animadex_abilitys_model(abilitydex["000"], abilitydex["000"], abilitydex["000"]), # Importante, poner abilities no abilitys
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 1,
        "catch_rate" : 255,
        "evolves": None,
        "base_stats" : animadex_base_stats_model(hp=250, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            4: techdex["000"],
        },
        "technique_capsules": { # Darle una vuelta a como poner esto, la key en orden 001, 002... o con la misma que en la techdex? oooo con la instancia/referencia de la capsula directamente
            "001" : techdex["000"],
        },
    }, 
    "001": { 
        "name": "starter", 
        "types": [TypeA.ESSENTIA, TypeB.NEUTRO],
        "abilitys": animadex_abilitys_model("", "", ""),
        "arcana": Arcana.TERRA,
        "growth": "parabolic",
        "exp_base_given": 64,
        "catch_rate": 45,
        "evolves": {"lvl" : 20, "to": "002"},
        "base_stats": animadex_base_stats_model(44, 40, 58, 62, 61, 49),
        "technique_learning": {
        },
        "technique_capsules": {
            "001" : techdex["000"],
        },     
    },
    "002": { 
        "name": "evolved_starter",
        "types": [TypeA.ESSENTIA, TypeB.LUX],
        "abilitys": "",
        "arcana": Arcana.TERRA,
        "growth": "parabolic",
        "exp_base_given": 141,
        "catch_rate" : 45,
        "evolves": {"lvl": 40, "to": "003"},
        "base_stats": animadex_base_stats_model(58, 54, 72, 79, 77, 56),
        "technique_learning": {
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "003": { 
        "name": "final_starter",
        "types": [TypeA.ESSENTIA, TypeB.LUX, TypeB.IGNIS],
        "abilitys": "",
        "arcana": Arcana.TERRA,
        "growth": "fast",
        "exp_base_given": 208,
        "catch_rate": 45,
        "evolves": None,
        "base_stats": animadex_base_stats_model(80, 68, 90, 121, 90, 70),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "004": {
        "name": "rival_starter",
        "types": [TypeA.UMBRA, TypeB.NEUTRO],
        "abilitys": "",
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 64,
        "catch_rate": 45,
        "evolves": {"lvl" : 20, "to": "005"},
        "base_stats": animadex_base_stats_model(hp=49, atk=55, sp_atk=44, _def=60, sp_def=60, spe=53),
        "technique_learning": {
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "005": { 
        "name": "evolved_rival_starter",
        "types": [TypeA.UMBRA, TypeB.SINISTER],
        "abilitys": "",
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 141,
        "catch_rate": 45,
        "evolves": {"lvl": 40, "to": "006"},
        "base_stats": animadex_base_stats_model(hp=61, atk=70, sp_atk=59, _def=81, sp_def=74, spe=61),
        "technique_learning": {
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "006": { 
        "name": "final_rival_starter",
        "types": [TypeA.UMBRA, TypeB.SINISTER, TypeB.AQUA],
        "abilitys": "",
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 208,
        "catch_rate": 45,
        "evolves": None,
        "base_stats": animadex_base_stats_model(hp=90, atk=92, sp_atk=61, _def=100, sp_def=113, spe=72),
        "technique_learning": {
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "007": {
        "name": "antagonist_starter",
        "types": [TypeA.FORMA, TypeB.NEUTRO],
        "abilitys": "",
        "arcana": Arcana.HALOS,
        "growth": "parabolic",
        "exp_base_given": 64,
        "evolves": {"lvl": 20, "to": "008"},
        "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), # modificar
        "technique_learning": {
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "008": {
        "name": "antagonist_evolved_starter",
        "types": [TypeA.FORMA, TypeB.VENENUM],
        "abilities": "",
        "arcana": Arcana.HALOS,
        "growth": "parabolic",
        "exp_base_given": 141,
        "evolves": {"lvl": 40, "to": "009"},
        "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
        },
        "assisted_techniques": {
        },
    },
    "009": {
        "name": "antagonist_final_starter",
        "types": [TypeA.FORMA, TypeB.VENENUM, TypeB.PLANTA],
        "abilities": "",
        "arcana": Arcana.HALOS,
        "growth": "parabolic",
        "exp_base_given": 208,
        "evolves": None,
        "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
        },
        "assisted_techniques": {            
        },
    },
    "010": {
      "name": "bird1",
      "types": [TypeA.NEUTRO, TypeB.VENTUS],
      "abilities": "",
      "arcana": Arcana.AURORA,
      "growth": "parabolic",
      "exp_base_given": 0,
      "catch_rate": 255,
      "evolves": {"lvl": 18, "to":"011"},
      "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
      "technique_learning": {
          
      },
      "assisted_techniques": {
          
      } 
    },
    "011": {
      "name": "bird1.2",
      "types": [TypeA.NEUTRO, TypeB.VENTUS],
      "abilities": "",
      "arcana": Arcana.AURORA,
      "growth": "parabolic",
      "exp_base_given": 0,
      "catch_rate": 255,
      "evolves": {"lvl": 34, "to": "012"},
      "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
      "technique_learning": {
          
      },
      "assisted_techniques": {
          
      } 
    },
    "012": {
      "name": "bird1.3",
      "types": [TypeA.NEUTRO, TypeB.VENTUS, TypeB.GLACIES],
      "abilities": "",
      "arcana": Arcana.AURORA,
      "growth": "parabolic",
      "exp_base_given": 0,
      "catch_rate": 255,
      "evolves": "011",
      "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
      "technique_learning": {
          
      },
      "assisted_techniques": {
          
      } 
    },
    "013": {
        "name": "bug1",
        "types": [TypeA.FORMA, TypeB.INSECTUM, TypeB.TERRA],
        "abilities": "",
        "arcana": Arcana.TERRA,
        "growth": "fast",
        "exp_base_given": 0,
        "catch_rate": 255,
        "evolves": "014",
        "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            
        }
    },
    "014": {
        "name": "bug1.2",
        "types": [TypeA.FORMA, TypeB.INSECTUM, TypeB.TERRA],
        "abilities": "",
        "arcana": Arcana.TERRA,
        "growth": "fast",
        "exp_base_given": 0,
        "catch_rate": 255,
        "evolves": ["015", "016"],
        "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            
        }
    },
    "015": {
        "name": "bug1.3.1",
        "types": [TypeA.FORMA, TypeB.INSECTUM, TypeB.TERRA],
        "abilities": "",
        "arcana": Arcana.TERRA,
        "growth": "fast",
        "exp_base_given": 0,
        "catch_rate": 255,
        "evolves": None,
        "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            
        }
    },
    "016": {
        "name": "bug1.3.2",
        "types": [TypeA.FORMA, TypeB.INSECTUM, TypeB.RUPES],
        "abilities": "",
        "arcana": Arcana.TERRA,
        "growth": "fast",
        "exp_base_given": 0,
        "catch_rate": 255,
        "evolves": None,
        "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            
        }
    },
    "017": {
        "name": "bug2",
        "types": [TypeA.UMBRA, TypeB.INSECTUM],
        "abilities": "",
        "arcana": Arcana.ECLIPSIS,
        "growth": "normal",
        "exp_base_given": 0,
        "catch_rate": 255,
        "evolves": "018",
        "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            
        }
    },
    "018": {
        "name": "bug2.2",
        "types": [TypeA.UMBRA, TypeB.INSECTUM, TypeB.PLANTA],
        "abilities": "",
        "arcana": Arcana.ECLIPSIS,
        "growth": "normal",
        "exp_base_given": 0,
        "catch_rate": 255,
        "evolves": None,
        "base_stats": animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            
        }
    },
    
}
'''A dictionary of every single Anima with its information that never changes'''
