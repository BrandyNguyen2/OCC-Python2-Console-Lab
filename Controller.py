# PROGRAMMER: Brandy Nguyen

from Controllers.KineticEnergyCalculatorController import kineticEnergyCalculatorController

class Controller :
    # CONSTRUCTOR
    def __init__(self, model, view) :
        self.__kineticEnergyCalculatorController = kineticEnergyCalculatorController( model.getKineticEnergyModel(), view.getKineticEnergyCalculatorView())