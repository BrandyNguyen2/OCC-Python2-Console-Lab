# PROGRAMMER: Brandy Nguyen 

from Model import Model
from View import View
from Controller import Controller 

def kineticEnergyApplication() :
    model = Model()
    view = View()
    controller = Controller(model, view)

kineticEnergyApplication()