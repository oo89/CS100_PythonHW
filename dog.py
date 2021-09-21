"""
Oscar Ojeda Perez
CS 100 2019F Section 105
HW 11, november 19, 2019
"""
class Dog:
    """Dog class definition"""
    # attribute
    species = "Canis familiaris"

    def __init__(self,_name,_breed):
        """ Constructor """
        #Assigning values
        self.name=_name
        self.breed=_breed
        self.tricks = []
    def teach(self, trick):
        """Add a passed string parameter to tricks"""
        #adding to the list 
        self.tricks.append(trick)
        #Printing 
        print(self.name + " knows " + trick )
    def knows(self, checkstr):
        """ check whether a passed string parameter is in the dog's list of tricks"""
        if checkstr in self.tricks:
            #printing message 
            print("Yes, " + self.name + " knows " + checkstr)
        else: 
            #printing message 
            print("No " + self.name + " doesn't know " + checkstr)
        
        





