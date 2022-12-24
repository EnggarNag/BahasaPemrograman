#Contoh mengakses function 
print ("Mengakses Function menggunakan Bahasa Pemrograman Python")
#void function 
def Penjumlahan():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    jumlah = a + b
    print ("Hasil  : ",jumlah)

def Pengurangan():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    kurang = a - b
    print ("Hasil  : ",kurang)

def Perkalian():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    kali = a * b
    print ("Hasil  : ",kali)

def Pembagian():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    bagi = a / b
    print ("Hasil  : ",bagi)

#Recursive Function
def Kalkulator():
    print ("=========Kalkulator=========")
    print ("1. Penjumlahan")
    print ("2. Pengurangan")
    print ("3. Perkalian")
    print ("4. Pembagian")
    print ("5. Exit")

while True:
    #untuk mengakses function cukup ketik nama function beserta tanda ()
    Kalkulator()
    pilih = int(input("Pilih Operasi Hitung : "))
    if pilih == 1:
        Penjumlahan()
    elif pilih == 2:
        Pengurangan()
    elif pilih == 3:
        Perkalian()
    elif pilih == 4:
        Pembagian()
    elif pilih == 5:
        break
    else:
        print ("pilihan tidak ada")

