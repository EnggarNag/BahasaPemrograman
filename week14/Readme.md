# Tugas 14

Penjelasan dan contoh program dari Encapsulation, Inheritance, dan Polymorphism menggunakan python

1.  Encapsulation
    Dalam contoh ini, kelas OVO memiliki atribut privat **balance, dan tiga method publik TopUp(), Transfer(), dan get_saldo(). Atribut **balance bersifat private, yang berarti hanya dapat diakses atau dimodifikasi di dalam kelas dan bukan dari luar. Method TopUp(), Transfer(), dan get_saldo() bersifat publik, yang berarti dapat diakses dari luar kelas.

    Metode TopUp() menambahkan jumlah tertentu ke saldo dan mengembalikan saldo baru. Metode Transfer() mengurangi jumlah yang ditentukan dari saldo, jika saldo mencukupi, dan mengembalikan saldo baru. Metode get_saldo() mengembalikan jumlah saldo saat ini.

    Contoh ini mendemonstrasikan enkapsulasi dengan menyembunyikan detail implementasi atribut \_\_saldo dan menyediakan tampilan publik untuk berinteraksi dengannya melalui method TopUp(), Transfer(), dan get_saldo(). Hal ini memungkinkan pengguna untuk berinteraksi dengan kelas tanpa harus mengetahui rincian bagaimana saldo disimpan atau dimanipulasi.

2.  Inheritance
    Dalam contoh ini, kelas Mobil mewarisi dari kelas Kendaraan. Ini berarti bahwa kelas Mobil memiliki akses ke semua atribut dan metode yang didefinisikan dalam kelas Kendaraan, dan juga dapat menambahkan atribut dan metode sendiri. Dalam hal ini, kelas Mobil meng-override metode print_value dan atribut value yang diwarisi dari kelas Kendaraan.

    Kelas yang mewarisi dari kelas lain disebut subkelas atau kelas turunan, dan kelas yang diwarisinya disebut superclass atau kelas dasar.

3.  Polymorphism
    Dalam contoh ini, kelas Bus dan Bike memiliki method yang disebut Horn() yang mengembalikan string. Fungsi get_transport() mengambil argumen "transport" dan mengembalikan objek dari kelas Bus atau Bike, berdasarkan nilai argumen.

    Kedua kelas memiliki method umum Horn(), dan fungsi get_transport() dapat memanggil method Horn() pada objek yang dikembalikan tanpa mengetahui kelas mana yang dimilikinya. Ini adalah contoh polimorfisme, karena method Horn() dapat dipanggil pada tipe objek yang berbeda (Bus dan Bike), tetapi method yang sama akan digunakan untuk melakukan aksi yang sama.

    Dalam contoh ini, fungsi get_transport() adalah contoh yang baik dari polimorfisme dalam aksi, karena dapat mengambil objek apapun, selama memiliki method Horn() dan akan bekerja dengan cara yang sama.
