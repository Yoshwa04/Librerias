import json
import tkinter as tk

class Translator():
    """
    This class serves to translate anything in a generic way using a json file.
    """
    
    def __init__(self, json_file: str, language: str="en"):
        """
        Inicializates the traductor in English by default.

        Args:
            json_file (str(.json)): The file with the translations.
            language (str, optional): The language wich will be translated. Defaults to "en".
        """
        
        self.language = language
        self.str = self.__load_json(json_file)
        
    
    def __load_json(self, json_file: str):
        try:
            with open(f"traduction_files\\{json_file.strip()}", "r", encoding="utf-8") as file:
                return json.load(file)
        except(FileNotFoundError, json.JSONDecodeError) as ex:
            raise ValueError(f"Error loading the file: {ex}")
    
    
    def translate(self, key: str):
        """
        Translates the key given.

        Args:
            key (str): The string you want to translate.

        Returns:
            str: The string translated
        """
        
        return self.str.get(self.language, {}).get(key, key)