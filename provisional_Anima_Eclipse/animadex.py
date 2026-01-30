from dataclasses import dataclass
from itertools import count
from typing import Callable, Literal, TypedDict

from arcana import Arcana
from type import TypeA, TypeB
from technique import Technique, techdex
from ability import Ability, abilitydex


_animadex_index = count(0)

def _next_animadex_key() -> str:
  return str(next(_animadex_index)).zfill(3)

@dataclass(slots=True)
class Animadex():
  name: str
  id: str
  types: tuple[TypeA, TypeB] | tuple[TypeA, TypeB, TypeB] 
  abilities: dict[str, str, str]
  arcana: Arcana
  growth: Literal["fast", "normal", "slow", "parabolic"] 
  exp_base_given: int
  catch_rate: int
  evolves: list[dict]
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
    growth: Literal["fast", "normal", "slow", "parabolic"], 
    exp_base_given: int, 
    catch_rate: int, 
    evolves: list[dict],
    base_stats: dict[str, int], 
    technique_learning: dict[int, str], 
    technique_capsules: tuple[str]
  ) -> tuple[str, Animadex]:
    animadex_id = _next_animadex_key()
      
    return animadex_id, Animadex(
      name=name,
      id=animadex_id,    
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
  Animadex._animadex_entry_model(
      "ejemplo", (TypeA.ESSENTIA, TypeB.AQUA), Animadex._animadex_abilities_model("001", "001", "001"), Arcana.ABYSSUS, "fast", 1, 255,
      [], 
      Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  
  Animadex._animadex_entry_model(
    "starter", (TypeA.ESSENTIA, TypeB.COMMUNIS), Animadex._animadex_abilities_model("", "",""), Arcana.TERRA, "parabolic", 64, 45,
    [{"method": "level", "value": "20", "to": "002"}], 
    Animadex._animadex_base_stats_model(hp=44, atk=40, sp_atk=58, _def=62, sp_def=61, spe=49), {}, ()
  ),
  Animadex._animadex_entry_model(
    "evolved_starter", (TypeA.ESSENTIA, TypeB.IGNIS), Animadex._animadex_abilities_model("", "",""), Arcana.TERRA, "parabolic", 141, 45,
    [{"method": "level", "value": "40", "to": "003"}], 
    Animadex._animadex_base_stats_model(hp=58, atk=54, sp_atk=72, _def=79, sp_def=77, spe=56), {}, ()
  ),
  Animadex._animadex_entry_model( ##### HAY QUE DARLE UN TIPO MAS 
    "final_starter", (TypeA.ESSENTIA, TypeB.IGNIS, TypeB.LUX), Animadex._animadex_abilities_model("", "",""), Arcana.TERRA, "parabolic", 208, 45,
    [], 
    Animadex._animadex_base_stats_model(hp=80, atk=68, sp_atk=90, _def=121, sp_def=90, spe=70), {}, ()
  ),
  Animadex._animadex_entry_model(
    "rival_starter", (TypeA.FORMA, TypeB.COMMUNIS), Animadex._animadex_abilities_model("", "",""), Arcana.ABYSSUS, "parabolic", 64, 45,
    [{"method": "level", "value": "20", "to": "005"}], 
    Animadex._animadex_base_stats_model(hp=49, atk=55, sp_atk=44, _def=60, sp_def=60, spe=53), {}, ()
  ),
  Animadex._animadex_entry_model(
    "evolved_rival_starter", (TypeA.FORMA, TypeB.AQUA), Animadex._animadex_abilities_model("", "",""), Arcana.ABYSSUS, "parabolic", 141, 45,
    [{"method": "level", "value": "40", "to": "006"}], 
    Animadex._animadex_base_stats_model(hp=61, atk=70, sp_atk=59, _def=81, sp_def=74, spe=61), {}, ()
  ),
  Animadex._animadex_entry_model(
    "final_rival_starter", (TypeA.FORMA, TypeB.AQUA, TypeB.SINISTER), Animadex._animadex_abilities_model("", "",""), Arcana.ABYSSUS, "parabolic", 208, 45,
    [], 
    Animadex._animadex_base_stats_model(hp=90, atk=92, sp_atk=61, _def=100, sp_def=113, spe=72), {}, ()
  ),
  Animadex._animadex_entry_model(
    "antagonist_starter", (TypeA.VOLUNTAS, TypeB.COMMUNIS), Animadex._animadex_abilities_model("", "",""), Arcana.HALOS, "parabolic", 64, 45,
    [{"method": "level", "value": "20", "to": "008"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "evolved_antagonist_starter", (TypeA.VOLUNTAS, TypeB.PLANTA), Animadex._animadex_abilities_model("", "",""), Arcana.HALOS, "parabolic", 141, 45,
    [{"method": "level", "value": "40", "to": "009"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "final_antagonist_starter", (TypeA.VOLUNTAS, TypeB.PLANTA, TypeB.VENENUM), Animadex._animadex_abilities_model("", "",""), Arcana.HALOS, "parabolic", 208, 45,
    [], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "bird1", (TypeA.NEUTRO, TypeB.VENTUS), Animadex._animadex_abilities_model("", "",""), Arcana.AURORA, "parabolic", 1, 200,
    [{"method": "level", "value": "18", "to": "011"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "bird1.2", (TypeA.NEUTRO, TypeB.VENTUS), Animadex._animadex_abilities_model("", "",""), Arcana.AURORA, "parabolic", 1, 200,
    [{"method": "level", "value": "34", "to": "012"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "bird1.3", (TypeA.NEUTRO, TypeB.VENTUS, TypeB.GLACIES), Animadex._animadex_abilities_model("", "",""), Arcana.AURORA, "parabolic", 1, 200,
    [], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "bug1", (TypeA.FORMA, TypeB.INSECTUM, TypeB.TERRA), Animadex._animadex_abilities_model("", "",""), Arcana.TERRA, "fast", 1, 255,
    [{"method": "level", "value": "12", "to": "014"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "bug1.2", (TypeA.FORMA, TypeB.INSECTUM, TypeB.TERRA), Animadex._animadex_abilities_model("", "",""), Arcana.TERRA, "fast", 1, 255,
    [
        {"method": "level", "value": "17", "to": "015"},
        {"method": "item", "value": "piedra_dura", "to": "016"}
    ],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "bug1.3.1", (TypeA.FORMA, TypeB.INSECTUM, TypeB.TERRA), Animadex._animadex_abilities_model("", "",""), Arcana.TERRA, "fast", 1, 255,
    [], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "bug1.3.2", (TypeA.FORMA, TypeB.INSECTUM, TypeB.RUPES), Animadex._animadex_abilities_model("", "",""), Arcana.COMETA, "fast", 1, 255,
    [], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "bug2", (TypeA.FORMA, TypeB.INSECTUM), Animadex._animadex_abilities_model("", "",""), Arcana.ECLIPSIS, "normal", 1, 255,
    [{"method": "level", "value": "12", "to": "018"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "bug2.2", (TypeA.FORMA, TypeB.INSECTUM, TypeB.PLANTA), Animadex._animadex_abilities_model("", "",""), Arcana.ECLIPSIS, "normal", 1, 255,
    [], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "normal1", (TypeA.NEUTRO, TypeB.COMMUNIS), Animadex._animadex_abilities_model("", "",""), Arcana.AURORA, "normal", 1, 230,
    [{"method": "level", "value": "18", "to": "020"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "normal1.2", (TypeA.NEUTRO, TypeB.COMMUNIS), Animadex._animadex_abilities_model("", "",""), Arcana.AURORA, "normal", 1, 230,
    [], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "pikachu1", (TypeA.VOLUNTAS, TypeB.ELECTRITAS), Animadex._animadex_abilities_model("", "",""), Arcana.COMETA, "normal", 1, 200,
    [{"method": "level", "value": "20", "to": "022"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "pikachu2", (TypeA.VOLUNTAS, TypeB.ELECTRITAS), Animadex._animadex_abilities_model("", "",""), Arcana.COMETA, "normal", 1, 200,
    [{"method": "item", "value": "piedra_trueno", "to": "023"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "pikachu3", (TypeA.VOLUNTAS, TypeB.ELECTRITAS), Animadex._animadex_abilities_model("", "",""), Arcana.COMETA, "normal", 1, 200,
    [], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "ghost1", (TypeA.ESSENTIA, TypeB.PHANTASMA, TypeB.TERRA), Animadex._animadex_abilities_model("", "",""), Arcana.LUNA, "normal", 1, 190,
    [{"method": "level", "value": "30", "to": "025"}], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "ghost1.2", (TypeA.ESSENTIA, TypeB.PHANTASMA, TypeB.TERRA), Animadex._animadex_abilities_model("", "",""), Arcana.LUNA, "normal", 1, 190,
    [], 
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {}, ()
  ),
  Animadex._animadex_entry_model(
    "eevee", (TypeA.NEUTRO, TypeB.COMMUNIS), Animadex._animadex_abilities_model("", "", ""), Arcana.TERRA, "normal", 00, 150,
    [
        {"method": "item", "value": "piedra_fuego", "to": "027"},
        {"method": "item", "value": "piedra_hielo", "to": "028"},
        {"method": "item", "value": "piedra_lunar", "to": "029"},
        {"method": "item", "value": "piedra_dura", "to": "030"}
    ],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "eeveeolution1", (TypeA.VOLUNTAS, TypeB.IGNIS), Animadex._animadex_abilities_model("", "", ""), Arcana.SOL, "normal", 00, 130,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "eeveeolution2", (TypeA.FORMA, TypeB.GLACIES), Animadex._animadex_abilities_model("", "", ""), Arcana.AURORA, "normal", 00, 130,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "eeveeolution3", (TypeA.ESSENTIA, TypeB.SINISTER), Animadex._animadex_abilities_model("", "", ""), Arcana.LUNA, "normal", 00, 130,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "eeveeolution4", (TypeA.FORMA, TypeB.RUPES), Animadex._animadex_abilities_model("", "", ""), Arcana.COMETA, "normal", 00, 130,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "steel1", (TypeA.FLUXOR, TypeB.METALLUM), Animadex._animadex_abilities_model("", "", ""), Arcana.HALOS, "slow", 00, 90,
    [{"method": "level", "value": "38", "to": "032"}],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "steel2", (TypeA.FLUXOR, TypeB.METALLUM, TypeB.PUGNA), Animadex._animadex_abilities_model("", "", ""), Arcana.HALOS, "slow", 00, 90,
    [{"method": "level", "value": "46", "to": "033"}],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "steel3", (TypeA.FLUXOR, TypeB.METALLUM, TypeB.PUGNA), Animadex._animadex_abilities_model("", "", ""), Arcana.HALOS, "slow", 00, 90,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "Ground1", (TypeA.NEUTRO, TypeB.TERRA), Animadex._animadex_abilities_model("", "", ""), Arcana.TERRA, "normal", 00, 90,
    [{"method": "level", "value": "27", "to": "035"}],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "Ground1.2", (TypeA.NEUTRO, TypeB.TERRA, TypeB.VENENUM), Animadex._animadex_abilities_model("", "", ""), Arcana.ZENITH, "normal", 00, 90,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "Fighting1", (TypeA.FLUXOR, TypeB.PUGNA), Animadex._animadex_abilities_model("", "", ""), Arcana.HALOS, "parabolic", 00, 90,
    [{"method": "item", "value": "piedra_fina", "to": "037"}],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "Fighting1.2", (TypeA.FLUXOR, TypeB.PUGNA), Animadex._animadex_abilities_model("", "", ""), Arcana.HALOS, "parabolic", 00, 90,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "Fighting2", (TypeA.ESSENTIA, TypeB.PUGNA), Animadex._animadex_abilities_model("", "", ""), Arcana.ECLIPSIS, "slow", 00, 90,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "Fighting3", (TypeA.VOLUNTAS, TypeB.PUGNA), Animadex._animadex_abilities_model("", "", ""), Arcana.NEBULA, "slow", 00, 90,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  
  
  
  
  
  
  
  
  Animadex._animadex_entry_model(
    "legendary1", (TypeA.ESSENTIA, TypeB.PSYCHICUS), Animadex._animadex_abilities_model("", "", ""), Arcana.ZENITH, "slow", 00, 3,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "legendary2", (TypeA.FORMA, TypeB.PUGNA), Animadex._animadex_abilities_model("", "", ""), Arcana.UNDAE, "slow", 00, 3,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
  Animadex._animadex_entry_model(
    "legendary3", (TypeA.VOLUNTAS, TypeB.LUX), Animadex._animadex_abilities_model("", "", ""), Arcana.SOL, "slow", 00, 3,
    [],
    Animadex._animadex_base_stats_model(hp=1, atk=1, sp_atk=1, _def=1, sp_def=1, spe=1), {4: techdex["000"]}, ("000")
  ),
    
}
'''A dictionary of every single Anima with its information that never changes'''



def _resolve_evolutions(animadex: dict[str, Animadex]):
  name_to_id = {a.name: k for k, a in animadex.items()}
  
  for anima in animadex.values():
    for evo in anima.evolves:
      evo["to"] = name_to_id[evo["to"]]

      
_resolve_evolutions(animadex)