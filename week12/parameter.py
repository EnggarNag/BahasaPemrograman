# fungsi yang dipanggil dengan parameter
def luas_segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi 
    print ("Luas Segitiga adalah :  ",luas )
 
def luas_PersegiPanjang(panjang, lebar):
    luasP = panjang * lebar
    print ("Luas Persegi Panjang adalah : ",luasP)

def deskripsi():
    print ("Menghitung Luas bangun datar dengan Parameter")
#Contoh mengakses function 
print ("Mengakses Function dengan parameter menggunakan Bahasa Pemrograman Python")
deskripsi()
print ("jika diketahui alas = 10 dan tinggi = 8 ,maka  " )
luas_segitiga(10, 8)
print ("jika diketahui panjang = 3 dan lebar = 4 ,maka  " )
luas_PersegiPanjang(3, 4)
