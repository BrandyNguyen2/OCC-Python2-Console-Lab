# PROGRAMMER: Brandy Nguyen 
from Views.KineticEnergyCalculatorView import KineticEnergyCalculatorView

class kineticEnergyCalculatorController :
    
    # CONSTRUCTOR
    def __init__(self, model, view) :
        self.__model = model
        self.__view = view 

        self.controlApplication()

    # METHODS
    def controlApplication(self) :
        selection = 0
        while selection != 4 : 
            #selection = KineticEnergyCalculatorView.mainMenu()
            pass
