from collections import defaultdict
from enum import Enum
from typing import DefaultDict

class TypeA(Enum):
    ESSENTIA = "Essentia"
    '''Essence'''
    FORMA = "Forma"
    UMBRA = "Umbra"
    '''Shadow'''
    FLUXOR = "Fluxor"
    '''Fluent'''
    NEUTRO = "Neutro"

class TypeB(Enum):   
    IGNIS = "Ignis"
    '''Fire'''
    AQUA = "Aqua"
    '''Water'''
    PLANTA = "Planta"
    '''Grass'''
    INSECTUM = "Insectum"
    '''Bug'''
    ELECTRITAS = "Electritas"
    '''Electric'''
    TERRA = "Terra"
    '''Ground'''
    VENTUS = "Ventus"
    '''Wind'''
    VENENUM = "Venenum"
    '''Poison'''
    METALLUM = "Metallum"
    '''Metal'''
    GLACIES = "Glacies"
    '''Ice'''
    LUX = "Lux"
    '''Light'''
    SINISTER = "Sinister"
    '''Dark'''
    PHANTASMA = "Phantasma"
    '''Ghost'''
    PSYCHICUS = "Psychicus"
    '''Psyquic'''
    RUPES = "Rupes"
    '''Rock'''
    PUGNA = "Pugna"
    '''Fighting'''
    NEUTRO = "Neutro"
    
    
effectiveness_chart: dict[TypeA | TypeB, DefaultDict[TypeA | TypeB, float]] = {
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