import json

from file_utils.json_utils import load_json

class Translator():
    """
    This class serves to translate anything in a generic way using a json file.
    """
    
    def __init__(
        self, 
        json_file: str, 
        language: str="en"
    ):
        """
        Inicializates the traductor in English by default.

        Args:
            json_file (str(.json)): The file with the translations.
            language (str, optional): The language wich will be translated. Defaults to english.
        """
        
        self.language = language
        self.str = load_json(json_file)
    
    
    def translate(self, key: str) -> str:
        """
        Translates the key given.

        Args:
            key (str): The string you want to translate.

        Returns:
            str: The string translated.
        """
        
        return self.str.get(self.language, {}).get(key, key)