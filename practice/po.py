class Plane:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")

class Cargo(Plane):
    def takeoff(self):
        print("cargo is takeoff")
    def fly(self):
        print("cargo plane is flying")
    def land(self):
        print("caargo plane is landing")
    

class Passenger(Plane):
    def takeoff(self):
        print("passenger is takeoff")
    def fly(self):
        print("passenger is flying")
    def land(self):
        print("passenger is landing")

class Fighter(Plane):
    def takeoff(self):
        print("fighter is takeoff")
    def fly(self):
        print("fighter is flying")
    def land(self):
        print("figther is landing")

c=Cargo()
p=Passenger()
f=Fighter()

def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
    
allowplane(c)
allowplane(p)
allowplane(f)
