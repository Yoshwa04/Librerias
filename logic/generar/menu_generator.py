from typing import Optional
from translator import Translator

class MenuGenerator():
    """
    This class generates console menus
    """
    
    def __init__(self, str_options, methods, json_options_file: Optional[str]=None, language: Optional[str]="en"):
        """
        Inicializates the menu generator in english by default and without a json needed.

        Args:
            str_options (list): A list of strings with the options in the console menu, can be with the key if a json used.
            methods (list): A list of methods for each option, the first and last position must be None.
            json_options (.json, optional): The name of the json file to be used with the different languages. Defaults to None.
            language (str, optional): The language of the menu to be generated. Defaults to "en".

        Raises:
            TypeError: If the two first arguments are not lists raises a TypeError.
            ValueError: If the two list lists have less than 3 index raises a ValueError.
        """
        
        error = False
        self._translator = Translator("menu_translations.json", language)
        self._options_translator = Translator(json_options_file, language) if json_options_file else None
        
        if (
            not isinstance(str_options, list) 
            or not isinstance(methods, list)
        ):
            error = True
            raise TypeError(self._translator.translate("type_error"))
        
        if len(str_options) < 3 or len(methods) < 3:
            error = True
            raise ValueError(self._translator.translate("value_error"))
        
        
        if not error:
            self._str_options = [
                self._options_translator.translate(opt) if self._options_translator and isinstance(opt, str) 
                else opt for opt in str_options
            ]
            self._methods = methods
            self.__def_menu_str_output()
        
    def menu_logic(self):
        """
        This method creates the logic of a menu with the provided methods to the class
        """
        
        self._user_option = -1
        
        while self._user_option != len(self._str_options) - 1:
            try:
                self.__ask_option_and_print_menu_output()
            
                if 0 <= self._user_option < len(self._methods) and self._user_option >= 1:
                    if self._methods[self._user_option] is not None:
                        self._methods[self._user_option]()
                    elif self._user_option == len(self._str_options) - 1:
                        print(
                            self._translator.translate("exiting") if self._str_options[-1] == self._translator.translate("exit") 
                            else self._translator.translate("going_back")
                            )
                else:
                    print(self._translator.translate("invalid_option"))
            except ValueError:
                print(self._translator.translate("invalid_option"))
        

    def __def_menu_str_output(self):
        menu_output = f"--------------------------\n"
        
        for i in range(1, len(self._str_options)):
            menu_output += f"{i} - {self._str_options[i]}\n"
            
        menu_output += f"--------------------------"
        
        self._menu_output = menu_output
    
    
    def __ask_option_and_print_menu_output(self):
        self._user_option = int(input(f"{self._menu_output}\n{self._str_options[0]}"))


def uno():
    print("Uno")
    
def dos(n):
    n2 = 2
    
    print(f"Suma: {n + n2}")
    
def tres():
    return 3




"""
Exemple:

o = ["menu_title", "option_1", "option_2", "option_3", "exit"]
m = [None, uno, lambda: dos(5), tres, None]

g = MenuGenerator(o, m, json_options="menu_test.json", language="en")

g.menu_logic()
"""
    

