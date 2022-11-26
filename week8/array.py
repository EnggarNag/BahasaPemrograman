from array import *
import array as exarray

ganjil = exarray.array('b',[1,3,5,7,9])
genap = exarray.array('b',[2,4,6,8])

#penggabungan array
gabungan = exarray.array('b')
gabungan = ganjil + genap

genap.insert(0,0) #masukan elemen bilangan 0 ke indeks 0

#cetak array
print("cetak Array")
print(ganjil) #cetak bilangan ganjil
print(genap) #cetak bilangan genap
print(gabungan) #cetak semua gabungan

#cetak elemen berdasarkan indeks
print("cetak dengan mengakses indeks")
print(ganjil[0]) #akses element indeks ke 0 
print(genap[-1]) #akses element terakhir
print(gabungan[4]) #akses element indeks ke 4

# Mencari dan mendapatkan indeks nilai dalam Array
print("cari indeks nilai 7 dalam array ganjil")
print(ganjil.index(7))

# menghapus elemen dari urutan list array
print("menghapus elemen dari urutan")
ganjil.pop(3)
print(ganjil)
# atau
del genap[4]
print(genap)

#menghapus nilai elemen dari array
print("menghapus 0 dari genap")
genap.remove(0)
print(genap)


