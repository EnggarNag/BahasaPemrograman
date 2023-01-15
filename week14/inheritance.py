class Kendaraan:
    def __init__(self):
        self.value = "Kendaraan Darat"
        
    def print_value(self):
        print(self.value)

class Mobil(Kendaraan):
    def __init__(self):
        self.value = "Mobil adalah kendaraan darat"

kendaraan = Kendaraan()
kendaraan.print_value() # prints "Kendaraan"

mobil = Mobil()
mobil.print_value() # prints "Mobil"
