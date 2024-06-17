class Vehicle:
    make = ""
    model = ""
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def moves(self):
        print("Moving Along...")
    
    def get_make_model(self):
        print(f"I'm a {self.make}, {self.model}.")

my_car = Vehicle("Tesla", "Model 3")

my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Caddilac", "Escalade")

your_car.get_make_model()
your_car.moves()

# Inheriting the vehicle class to more specific vehicles

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        self.faa_id = faa_id
        super().__init__(make, model)
    # method is overridden
    def moves(self):
        print("Flying Along...")
    def get_make_model(self):
        super().get_make_model()
        print(f'faa_id = {self.faa_id}')

class Truck(Vehicle):
    def moves(self):
        print("Rumbles Along...")

class GolfCart(Vehicle):
    # since a class cannot be empty and we are not adding any functionality specific to this class 
    pass

cesna = Airplane('Cessna', 'Skyhawk', 'FAA01')
truck = Truck('Mac', 'Pinaccle')
golf = GolfCart('Yamaha', 'GC100')

cesna.get_make_model()
cesna.moves()

truck.get_make_model()
truck.moves()

golf.get_make_model()
golf.moves()

print('\n\n')

# example of polymorphism because the get_make_model and the moves function behaves differently in different scenarios
for v in (my_car, your_car, truck, cesna, golf):
    v.get_make_model()
    v.moves()
