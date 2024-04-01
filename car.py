class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def display_info(self):
        print(f"Car: {self.make} {self.model}")

C1=Car('Toyota','Corolla')
C2=Car('Honda','Civic')
print(C1.display_info())
print(C2.display_info())