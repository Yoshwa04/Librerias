from arcana import Arcana
from confident import Confident
from trainer_base import TrainerBase


"""El jugador debe tener como info propia: 
    - La fase del juego en la que esta, es decir, a que bosses de la historia a derrotado
    - El inventario, separado por clase de objeto y cuantos tiene (si tiene 0 pues evidentemente no miostraria nada)
    - Su equipo actual de animas seleccionadas que luchan en combates
    - Su "caja" de animas que no participan, en la reserva
    - el nivel con sus confidentes (de 0(no desbloqueado) a 10)"""
class Player(TrainerBase):
    def __init__(self, name, money):
        super().__init__(name, money)
        
        for arcana in Arcana:
            confident = Confident(
                name=arcana.value,
                arcana=arcana,
            )
            self.confidents[arcana] = confident