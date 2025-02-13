class Transport:
    def __init__(self, name, speed):
        self.name=name
        self.speed=speed


    def info(self):
        print(f"Bu mashina nomi {self.name}, tezligi {self.speed}")


class Car(Transport):
    def info(self):
        print(f"Bu mashina nomi {self.name}, tezligi {self.speed}")


class Bicycle(Transport):
    def info(self):
        print(f"Bu velosiped nomi {self.name}, tezligi {self.speed}")



c=Car("Nexia 2", 280)
c.info()

b=Bicycle("Gonka", 30)
b.info()

t=Transport("AUDI", 300)
t.info()


