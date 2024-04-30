# PROGRAMMER: Brandy Nguyen

class KineticEnergyCalculatorView :
    # CONSTRUCTOR

    # METHODS
    def mainMenu(self) :
        print()
        print("Main Menu")
        print("1. Enter Mass")
        print("2. Enter Velocity")
        print("3. Calculate Kinetic Energy")
        print("4. Exit")
        try :
            userInput = int( input("Enter your selection"))
            if userInput == 1 :
                KineticEnergyCalculatorView.massInput()
                return userInput
            elif userInput == 2 :
                KineticEnergyCalculatorView.velocityInput()
                return userInput
            elif userInput == 3 :
                KineticEnergyCalculatorView.kineticEnergyOutput()
                return userInput
            else : 
                return userInput
        except BaseException as exceptionObject :
            print("Main Menu: ", exceptionObject)
            return 0
        
    def massInput(self) :
        self.__mass = float(input("Enter Mass: "))
        if self.__mass <= 0 :
            raise ValueError("Mass must be greater than 0")
        else :
            return self.__mass

    def velocityInput(self) :
        self.__velocity = float(input("Enter Velocity: "))
        if self.__velocity <= 0 :
            raise ValueError("Velocity must be greater than 0")
        else :
            return self.__velocity

    def kineticEnergyOutput(self, mass, velocity, kineticEnergy) :
        print("")
        print("Mass: ", mass)
        print("Velocity: ", velocity)
        print("Kinetic Energy: ", kineticEnergy)
