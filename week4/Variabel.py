#variabel
a = "Enggar Lanang Nandhito Agil Ghibran"
def func():
    a = "any"
    print ("Selamat " + a)
func()
print (a)

#definisi
def tambah():
    a = 5
    b = 3
    c = a+b
    print (c)

tambah()

#definisi parameter
def data(nama,nim):
    print(f"Nama Saya {nama} dan {nim}")
data("Enggar LNAG","20200801076")

#contoh 
def total(sisi):
    return sisi*sisi
def segitiga(alas,tinggi):
    return 0.5*alas*tinggi
    