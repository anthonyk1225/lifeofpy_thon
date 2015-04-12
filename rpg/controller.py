from views import *
from model import *

class Controller:
    def __init__(self):
        self.hero = Hero()
        self.view = View()

    def startup(self):
        if self.view.battle()==1:
            self.enemy = Goblin()
        elif self.view.battle()==2:
            self.enemy = Orc()
        else:
            self.enemy = Ogre()
