import os
import sys
from typing import List, Optional
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from translator import Translator


class Menu:
    def __init__(
        self, 
        methods_list: List, 
        options_list: List[str], 
        lan: str = "en", 
        json_file: str = None,
    ):
        """_summary_

        Args:
            methods_list (List): list with the methods for each option
            options_list (List[str]): the keys of the options (for the json or for literally print)
            lan (str, optional): language of the menu. Defaults to "en".
            json_file (str, optional): json file with the translations. Defaults to None.
        """
        self.methods = methods_list
        self.options = options_list
        
        self.translator = Translator(json_file, lan) if json_file else None
        self.lan = lan
        self.system_translator = Translator("menu_self_texts.json", lan)    
        
        
        
    def _get_text(self, key: str) -> str:
        if self.translator:
            return self.translator.translate(key)
        return key
    
    def _sys_text(self, key: str) -> str:
        return self.system_translator.translate(key)
    
    
    def _print(self):
        print("\n---------------------------------")
            
        title = self._get_text(self.options[0])
        print(title)
            
        print("---------------------------------")

        for i in range(1, len(self.options) - 1):
            text = self._get_text(self.options[i])
            print(f"{i} - {text}")
                
        last_text = self._get_text(self.options[-1])
        print(f"{i+1} - {last_text}")
        print("---------------------------------")
    
    def show(self):
        opt = -1
        while True:
            self._print()
            
            try:
                opt = int(input(self._sys_text("choose_option")))
            except ValueError:
                print(self._sys_text("must_be_a_number"))
                continue

            if opt <= 0 or opt > len(self.methods):
                print(self._sys_text("invalid_option"))
                continue
            elif 0 <= opt < len(self.methods) - 1 and opt >= 1:
                if self.methods[opt] is not None:
                    self.methods[opt]()
                    continue
            elif opt is len(self.methods) - 1:
                print(self.system_translator.translate("exit")) if self.options[-1] == "Exit" or self.options[-1] == "Salir" else print(self.system_translator.translate("go_back"))
                return
                
                
# def opcion1():
#     print("Has elegido la opción 1")
    
# options2 = ["Menú 2", "Opción 1", "Retroceder"]
# methods2 = [None, opcion1, None]
# menu2 = Menu(methods2, options2, "es")


# methods = [None, opcion1, lambda: menu2.show(), None]
# options = ["Menú Principal", "Opción 1", "Submenú", "Salir"]

# menu = Menu(methods, options, "es")
# menu.show()