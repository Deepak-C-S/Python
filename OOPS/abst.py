# class Engine:
#     def start(self):
#         pass
#     def stop(self):
#         pass
class petrolEngine:
    def start(self):
        print("Petrol engine started")
    def stop(self):
        print("Petrol engine stopped")
class dieselEngine:
    def start(self):
        print("Diesel engine started")
    def stop(self):
        print("Diesel engine stopped")
class car:
    def __init__(self,engine):
        self.engine=engine
    def startEngine(self):
        self.engine.start()
    def stopEngine(self):
        self.engine.stop()
p=petrolEngine()
d=dieselEngine()
c=car(p)
c.startEngine()
c.stopEngine()