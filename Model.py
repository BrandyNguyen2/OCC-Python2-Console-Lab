# PROGRAMMER: Brandy Nguyen 

from Models.KineticEnergy import KineticEnergy

class Model :
    # CONSTRUCTOR
    def __init__(self) :
        self.__kineticEnergyModel = KineticEnergy()

    def getKineticEnergyModel(self) :
        return self.__kineticEnergyModel