from trainer_base import TrainerBase

class TrainerAI(TrainerBase):
    def __init__(self, name, money, team):
        super().__init__(name, money)
        
        self.team = team
        
        