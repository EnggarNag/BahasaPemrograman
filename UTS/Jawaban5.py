#Ordering Drink
def menu():
    x = "capucino"
    y = "teh"
    print ("Pilihan")
    print ("1.", x)
    print ("2.", y)
    print ("3. Exit")

def capucino():
    print("memilih capucino")
    harga = int(input("masukkan harga : "))
    ppn = harga*10/100
    total = harga + ppn
    print("Jumlah yang harus dibayarkan ", total)

def teh():
    print("memilih Teh")
    harga = int(input("masukkan harga : "))
    ppn = harga*10/100
    total = harga + ppn
    print("Jumlah yang harus dibayarkan ", total)

def biodata():
    nim = 20200801076
    nama = "Enggar Lanang N A G "
    print ("NIM  : ", nim)
    print ("NAMA : ", nama)

while True:
    biodata()
    menu()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")