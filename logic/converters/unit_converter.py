from typing import Union

Number = Union[int, float]

def km_to_m(km: Number) -> float:
    """Converts kilometers to meters"""
    return km * 1000

def m_to_km(m: Number) -> float:
    """Converts meters to kilometers"""
    return m / 1000

def cm_to_m(cm: Number) -> float:
    """Converts centimeters to meters"""
    return cm / 100

def m_to_cm(m: Number) -> float:
    """Converts meters to centimeters"""
    return m * 100

def kg_to_g(kg: Number) -> float:
    """Converts kilograms to grams"""
    return kg * 1000

def g_to_kg(g: Number) -> float:
    """Converts grams to kilograms"""
    return g / 1000

def lb_to_kg(lb: Number) -> float:
    """Converts pounds to kilograms"""
    return lb * 0.45359237

def kg_to_lb(kg: Number) -> float:
    """Converts kilograms to pounds"""
    return kg / 0.45359237


