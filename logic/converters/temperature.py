from typing import Union

Number = Union[int, float]

def celsius_to_fahrenheit(c: Number) -> float:
    """Converts Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: Number) -> float:
    """Converts Fahrenheit to Celsius"""
    return (f - 32) * 5/9

def celsius_to_kelvin(c: Number) -> float:
    """Converts Celsius to Kelvin"""
    return c + 273.15

def kelvin_to_celsius(k: Number) -> float:
    """Converts Kelvin to Celsius"""
    return k - 273.15

def fahrenheit_to_kelvin(f: Number) -> float:
    """Converts Fahrenheit to Kelvin"""
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k: Number) -> float:
    """Converts Kelvin to Fahrenheit"""
    return celsius_to_fahrenheit(kelvin_to_celsius(k))
