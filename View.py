# PROGRAMMER: Brandy Nguyen 

from Views.KineticEnergyCalculatorView import KineticEnergyCalculatorView

class View :
    # CONSTRUCTOR
    def __init__(self) :
        self.__kineticEnergyCalculatorView = KineticEnergyCalculatorView()

    # METHODS
    def getKineticEnergyCalculatorView(self) :
        return self.__kineticEnergyCalculatorView