# PROGRAMMER: Brandy Nguyen 

class KineticEnergy :
    # CONSTRUCTOR
    def __init__(self) :
        self.__mass = None
        self.__velocity = None
        self.__kineticEnergy = None
    # METHODS
    def getMass(self) :
        return self.__mass
    
    def getVelocity(self) :
        return self.__velocity
    
    def getKineticEnergy(self) :
        return self.__kineticEnergy
    
    def setMass(self, mass) :
        self.__mass = mass

    def setVelocity(self, velocity) :
        self.__velocity = velocity

    def calculateKineticEnergy(self) :
        return 0.5 * (self.__mass * (self.__velocity ** 2))