class Bus:
    def __init__(self, nama):
        self.nama = nama
        
    def Horn(self):
        return "Telolet!"

class Bike:
    def __init__(self, merk):
        self.merk = merk
        
    def Horn(self):
        return "Kring Kring!"

def get_transport(transport):
    transports = {
        "Bus": Bus("Bulan Jaya"),
        "Bike": Bike("Polygon")
    }
    return transports[transport]

d = get_transport("Bus")
print(d.Horn())

c = get_transport("Bike")
print(c.Horn())
