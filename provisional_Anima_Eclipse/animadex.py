from dataclasses import dataclass
from typing import Callable, Literal, TypedDict

from arcana import Arcana
from type import TypeA, TypeB
from technique import Technique, techdex
from ability import Ability, abilitydex

@dataclass(slots=True)
class Animadex():
    name: str
    types: tuple[TypeA, TypeB] | tuple[TypeA, TypeB, TypeB] 
    abilities: dict[str, str, str]
    arcana: Arcana
    growth: str
    exp_base_given: int
    catch_rate: int
    evolves: str | dict[str, str] | None
    base_stats: dict[str, int]
    technique_learning: dict[int, str]
    technique_capsules: tuple[str]
    
    def _animadex_base_stats_model(hp: int, atk: int, sp_atk: int, _def: int, sp_def: int, spe: int) -> dict[str, int]:
        '''This method just returns a dict of the stats given its value'''
        return {
            "hp" : hp,
            "atk" : atk,
            "sp_atk" : sp_atk,
            "def" : _def,
            "sp_def" : sp_def,
            "spe" : spe,  
        }
        
    def _animadex_abilities_model(ability1: str, ability2: str, hidden: str) -> dict[str, Ability]:
        '''This method just returns a dict of the abilitys given'''
        return {
            "001" : ability1,
            "002" : ability2,
            "00H" : hidden,  
        }
        
    def _animadex_entry_model(
        name: str, 
        types: tuple[TypeA, TypeB] | tuple[TypeA, TypeB, TypeB],
        abilities: dict[str, str, str], 
        arcana: Arcana, 
        growth: Literal["fast", "nomral", "slow", "parabolic"], 
        exp_base_given: int, 
        catch_rate: int, 
        evolves: str | None, 
        base_stats: dict[str, int], 
        technique_learning: dict[int, str], 
        technique_capsules: tuple[str]
    ) -> Animadex:
        return Animadex(
            name=name,    
            types=types,
            abilities=abilities,
            arcana=arcana,
            growth=growth,
            exp_base_given=exp_base_given,
            catch_rate=catch_rate,
            evolves=evolves,
            base_stats=base_stats,
            technique_learning=technique_learning,
            technique_capsules=technique_capsules
        )


animadex: dict[str, Animadex] = {
    # Ejemplo usando el método
    "000": Animadex._animadex_entry_model(
        "ejemplo", (TypeA.ESSENTIA, TypeB.AQUA), Animadex._animadex_abilities_model("001", "001", "001"), Arcana.ABYSSUS, "fast", 1, 255, None, 
        Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "001": { 
        "name": "starter", 
        "types": [TypeA.ESSENTIA, TypeB.COMMUNIS],
        "abilitys": Animadex._animadex_abilities_model("", "", ""),
        "arcana": Arcana.TERRA,
        "growth": "parabolic",
        "exp_base_given": 64,
        "catch_rate": 45,
        "evolves": {"lvl" : 20, "to": "002"},
        "base_stats": Animadex._animadex_base_stats_model(44, 40, 58, 62, 61, 49),
        "technique_learning": {
        },
        "technique_capsules": {
            "001" : techdex["000"],
        },
    },
    "002": { 
        "name": "evolved_starter",
        "types": [TypeA.ESSENTIA, TypeB.LUX, TypeB.IGNIS],
        "abilitys": "",
        "arcana": Arcana.TERRA,
        "growth": "parabolic",
        "exp_base_given": 141,
        "catch_rate" : 45,
        "evolves": {"lvl": 40, "to": "003"},
        "base_stats": Animadex._animadex_base_stats_model(58, 54, 72, 79, 77, 56),
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
        "base_stats": Animadex._animadex_base_stats_model(80, 68, 90, 121, 90, 70),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "004": {
        "name": "rival_starter",
        "types": [TypeA.FORMA, TypeB.COMMUNIS],
        "abilitys": "",
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 64,
        "catch_rate": 45,
        "evolves": {"lvl" : 20, "to": "005"},
        "base_stats": Animadex._animadex_base_stats_model(hp=49, atk=55, sp_atk=44, _def=60, sp_def=60, spe=53),
        "technique_learning": {
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "005": { 
        "name": "evolved_rival_starter",
        "types": [TypeA.FORMA, TypeB.SINISTER],
        "abilitys": "",
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 141,
        "catch_rate": 45,
        "evolves": {"lvl": 40, "to": "006"},
        "base_stats": Animadex._animadex_base_stats_model(hp=61, atk=70, sp_atk=59, _def=81, sp_def=74, spe=61),
        "technique_learning": {
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "006": { 
        "name": "final_rival_starter",
        "types": [TypeA.FORMA, TypeB.SINISTER, TypeB.AQUA],
        "abilitys": "",
        "arcana": Arcana.ABYSSUS,
        "growth": "parabolic",
        "exp_base_given": 208,
        "catch_rate": 45,
        "evolves": None,
        "base_stats": Animadex._animadex_base_stats_model(hp=90, atk=92, sp_atk=61, _def=100, sp_def=113, spe=72),
        "technique_learning": {
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "007": {
        "name": "antagonist_starter",
        "types": [TypeA.VOLUNTAS, TypeB.COMMUNIS],
        "abilitys": "",
        "arcana": Arcana.HALOS,
        "growth": "parabolic",
        "exp_base_given": 64,
        "evolves": {"lvl": 20, "to": "008"},
        "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), # modificar
        "technique_learning": {
        },
        "assisted_techniques": {
            "001" : techdex["000"],
        },
    },
    "008": {
        "name": "antagonist_evolved_starter",
        "types": [TypeA.VOLUNTAS, TypeB.VENENUM],
        "abilities": "",
        "arcana": Arcana.HALOS,
        "growth": "parabolic",
        "exp_base_given": 141,
        "evolves": {"lvl": 40, "to": "009"},
        "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
        },
        "assisted_techniques": {
        },
    },
    "009": {
        "name": "antagonist_final_starter",
        "types": [TypeA.VOLUNTAS, TypeB.VENENUM, TypeB.PLANTA],
        "abilities": "",
        "arcana": Arcana.HALOS,
        "growth": "parabolic",
        "exp_base_given": 208,
        "evolves": None,
        "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
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
      "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
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
      "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
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
      "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
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
        "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
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
        "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
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
        "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
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
        "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            
        }
    },
    "017": {
        "name": "bug2",
        "types": [TypeA.VOLUNTAS, TypeB.INSECTUM],
        "abilities": "",
        "arcana": Arcana.ECLIPSIS,
        "growth": "normal",
        "exp_base_given": 0,
        "catch_rate": 255,
        "evolves": "018",
        "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            
        }
    },
    "018": {
        "name": "bug2.2",
        "types": [TypeA.VOLUNTAS, TypeB.INSECTUM, TypeB.PLANTA],
        "abilities": "",
        "arcana": Arcana.ECLIPSIS,
        "growth": "normal",
        "exp_base_given": 0,
        "catch_rate": 255,
        "evolves": None,
        "base_stats": Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1),
        "technique_learning": {
            
        },
        "assisted_techniques": {
            
        }
    },

    "019": Animadex._animadex_entry_model(
      "normal1", (TypeA.NEUTRO, TypeB.COMMUNIS), Animadex._animadex_abilities_model("", "", ""), Arcana.AURORA, "normal", 00, 230, "18:020",
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "020": Animadex._animadex_entry_model(
      "normal1.2", (TypeA.NEUTRO, TypeB.COMMUNIS), Animadex._animadex_abilities_model("", "", ""), Arcana.AURORA, "normal", 00, 230, None,
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    
    "021": Animadex._animadex_entry_model(
      "electric1", (TypeA.VOLUNTAS, TypeB.ELECTRITAS), Animadex._animadex_abilities_model("", "", ""), Arcana.COMETA, "normal", 00, 200, "20:022",
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "022": Animadex._animadex_entry_model(
      "electric1.2", (TypeA.VOLUNTAS, TypeB.ELECTRITAS), Animadex._animadex_abilities_model("", "", ""), Arcana.COMETA, "normal", 00, 200, "28:023",
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "023": Animadex._animadex_entry_model(
      "electric1.3", (TypeA.VOLUNTAS, TypeB.ELECTRITAS), Animadex._animadex_abilities_model("", "", ""), Arcana.COMETA, "normal", 00, 200, None,
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    
    "024": Animadex._animadex_entry_model(
      "Ghost", (TypeA.ESSENTIA, TypeB.PHANTASMA, TypeB.TERRA), Animadex._animadex_abilities_model("", "", ""), Arcana.LUNA, "normal", 00, 190, "30:025",
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "025": Animadex._animadex_entry_model(
      "Ghost", (TypeA.ESSENTIA, TypeB.PHANTASMA, TypeB.TERRA), Animadex._animadex_abilities_model("", "", ""), Arcana.LUNA, "normal", 00, 190, None,
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    
    "026": Animadex._animadex_entry_model(
      "eevee", (TypeA.NEUTRO, TypeB.COMMUNIS), Animadex._animadex_abilities_model("", "", ""), Arcana.TERRA, "normal", 00, 150,
      {"piedra_fuego": "027",
       "piedra_hielo": "028",
       "piedra_lunar": "029",
       "piedra_dura": "030"},
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "027": Animadex._animadex_entry_model(
      "eeveeolution1", (TypeA.VOLUNTAS, TypeB.IGNIS), Animadex._animadex_abilities_model("", "", ""), Arcana.SOL, "normal", 00, 130, None,
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "028": Animadex._animadex_entry_model(
      "eeveeolution2", (TypeA.FORMA, TypeB.GLACIES), Animadex._animadex_abilities_model("", "", ""), Arcana.AURORA, "normal", 00, 130, None,
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "029": Animadex._animadex_entry_model(
      "eeveeolution3", (TypeA.ESSENTIA, TypeB.SINISTER), Animadex._animadex_abilities_model("", "", ""), Arcana.LUNA, "normal", 00, 130, None,
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "030": Animadex._animadex_entry_model(
      "eeveeolution4", (TypeA.FORMA, TypeB.RUPES), Animadex._animadex_abilities_model("", "", ""), Arcana.COMETA, "normal", 00, 130, None,
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    
    "031": Animadex._animadex_entry_model(
      "steel1", (TypeA.FLUXOR, TypeB.METALLUM), Animadex._animadex_abilities_model("", "", ""), Arcana.HALOS, "slow", 00, 90, "38:032",
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "032": Animadex._animadex_entry_model(
      "steel2", (TypeA.FLUXOR, TypeB.METALLUM, TypeB.PUGNA), Animadex._animadex_abilities_model("", "", ""), Arcana.HALOS, "slow", 00, 90, "44:033",
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    "033": Animadex._animadex_entry_model(
      "steel3", (TypeA.FLUXOR, TypeB.METALLUM, TypeB.PUGNA), Animadex._animadex_abilities_model("", "", ""), Arcana.HALOS, "slow", 00, 90, None,
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
    ),
    
}
'''A dictionary of every single Anima with its information that never changes'''



# Metodo provisional y no acabado, no se si ira aqui para separar la informacion de la evolucion de un anima y tener por separado el nivel necesario (o otra cosa supongo) y a cual evoluciona
def __split_lvl_and_animadex(str: str):
    lvl = int(str.split(":")[0])
    animadex_number = lvl = str.split(":")[1]