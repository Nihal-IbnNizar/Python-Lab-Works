class Car:
    def __init__(self,brand,model):
        self.brand =  brand
        self.model = model
        
    def move(self):
        print("Drive")
        
class Boat:
    def __init__(self,brand,model):
        self.brand =  brand
        self.model = model
        
    def move(self):
        print("Sail")
        
class Airplane:
    def __init__(self,brand,model):
        self.brand =  brand
        self.model = model
        
    def move(self):
        print("Fly")
        
car1 = Car("Nissan","GTR")
boat1 = Boat("Ibiza","Touring 20")
plane1 = Airplane("Boeing","747")

car1.move()
for x in (boat1,plane1):
    print(x.brand,x.model)
    x.move()