# Contoh Penanganan kesalahan saat mengambil input dari user dalam program menghitung pembagian
try:
    a = int(input("Masukan angka pertama : "))
    b = int(input("Masukan angka kedua : "))
    print(a / b)
except ValueError:
    print("Error: Invalid input. Masukan angka yang valid.")
except ZeroDivisionError:
    print("Error: Tidak dapat dibagi nol")