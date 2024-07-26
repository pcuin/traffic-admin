# traffic

class Traffic:

    def __init__(self, radius, risk, HOV, speed):
        tiers = {"Low": 1, "Moderate": 2, "High": 3}
        self.risk = tiers.get(risk)# val
        self.rkey = risk # key

        
        self.radius = int(radius) # int
        
        self.carpool = HOV # booleans
        self.speed = speed # booleans
        self.driver = "solo" # str

    def __str__(self):
        if self.carpool is True:
            self.driver = "carpool"

        if self.speed is True:
            self.speed = "Autobahn zone"
        self.speed = "65 MAX zone"

        return f"You are within {self.radius} mile(s) of your destination. \n\
Considering {self.rkey} liability, as a {self.driver} driver,\n\
in the {self.speed} lane."

    def get_liability(self):
        return self.risk


d = Traffic(1.99, "Low", 0, 1)
print(d.get_liability()) 








        
