# Variabel dan Type Data

# Variabel

Definisi Variabel adalah lokasi memori yang dicadangkan untuk menyimpan nilai-nilai.
Fungsi variabel merupakan tempat penyimpanan data yang bersifat mutable, artinya nilainya bisa berubah-ubah. Variabel dapat berisi teks maupun bilangan.
Variabel dapat menyimpan berbagai macam tipe data. Di dalam pemrograman Python, variabel mempunyai sifat yang dinamis, artinya variabel Python tidak perlu didekralasikan tipe data tertentu dan variabel Python dapat diubah saat program dijalankan. Variabel dalam python memiliki format penulisan nama_variabel = <nilai>

# Type data

Tipe data adalah klasifikasi variable untuk menentukan data yang akan disimpan ke dalam memori.
Python sendiri mempunyai tipe data yang cukup unik bila kita bandingkan dengan bahasa pemrograman yang lain.
Berikut adalah tipe data dari bahasa pemrograman Python :

1. tipe data Boolean
   Tipe data boolean adalah tipe data yang hanya memiliki 2 nilai yaitu True dan False. Biasa digunakan dalam kebutuhan conditional programming.
   contoh :
   print(True)

   i = True
   print (type(i))
   .

2. tipe data String
   Tipe data string berfungsi untuk menyatakan huruf / kalimat yang berupa angka, tulisan atau pun karakter khusus. Pendeklarasian variable untuk tipe string diapit oleh " atau '.
   contoh :
   print("Hello World dengan Python")
   print('Ini bahasa Python')

   a = "hello world"
   print (a)
   print (type(a))
   .

3. tipe data Integer
   Tipe data integer berfungsi untuk menyatakan angka bilangan bulat. Berbeda dengan tipe string, tipe data tipe integer dapat diaplikasikan pada operasi matematika.
   contoh integer :
   b = 90
   print (b)
   print (type(b))

   print (2022)
   .

4. tipe data Float
   Tipe data float berfungsi untuk menyatakan angka bilangan desimal.
   contoh float :
   c = 10.5
   print (c)
   print (type(c))

   print (3.14)
   .

5. tipe data Hexadecimal
   Tipe data hexadecimal berfungsi untuk sistem bilangan basis 16 , sebuah sistem bilangan yang menggunakan 16 simbol dengan urutan angka sebagai berikut 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
   print(9a)
   .
6. tipe data Complex
   Tipe data complex berfungsi untuk menyatakan angka real dan imajiner. Bilangan imajiner adalah bilangan yang diperoleh dari akar bilangan rasional negatif.
   contoh data complex :
   e = 1j
   print (e)
   print (type(e))

   z = complex ('5-9j')
   print (z)
   print(5j)

7. tipe data List
   Tipe data list adalah sebuah urutan (sequence) dari kumpulan data yang dapat diubah - ubah (Flexibel). Data list dapat didefinisikan dengan [] atau list().
   contoh type data list :
   f = ["a","b","c"]
   print (f)
   print (type(f))

   list_f = [1,2,3]
   print (list_f[0])

   print([1,2,3,4,5])
   print(["satu", "dua", "tiga"])

8. tipe data Tuple
   Tipe data tupple adalah sebuah urutan (sequence) untuk menyimpan beberapa data yang tidak dapat diubah - ubah (Fixed). Data tupple dapat didefinisikan dengan () atau tuple().
   contoh tuple :
   d = 20,5
   print (d)
   print (type(d))

   tuple_f = 1,2,3
   print (tuple_f[0])

   print((1,2,3,4,5))
   print(("satu", "dua", "tiga"))

9. Tipe data set
   Tipe data set adalah tipe data yang terdiri dari kelompok data yang sama (uniqe). Sehingga data yang ada didalamnya tidak boleh ada yang sama. Jika ada yang sama maka akan melebur menjadi satu.
   contoh type data set :
   g = {"a","b","c"}
   print (g)
   print (type(g))

   contoh set :
   set_f = {1,2,3}
   print (set_f)

   type data frozenset berfungsi untuk mengubah iterable menjadi objek set yang tidak bisa diubah (immutable). Frozenset adalah versi immutable dari set
   h = frozenset({1,2,3})
   print (type(h))

10. tipe data Dictionary
    Tipe data dictionary adalah jenis array untuk menyimpan beberapa pasang data yang memiliki “key” untuk penunjuk value.
    print({"nama":"Budi", 'umur':20})

    tipe data Dictionary dimasukan ke dalam variabel biodata

    biodata = {"nama":"Andi", 'umur':21} #proses inisialisasi variabel biodata
    print(biodata) #proses pencetakan variabel biodata yang berisi tipe data Dictionary
    print(type(biodata)) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'> yang berarti dict adalah tipe
    data dictionary
