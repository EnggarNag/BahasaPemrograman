import mysql.connector

# Koneksi ke database
nagdb = mysql.connector.connect(
    user='root', 
    passwd='password', 
    host='127.0.0.1',
    port=3306)

if nagdb.is_connected():
  print("Berhasil terhubung ke database")
# membuat Cursor
#db = nagdb.cursor()
# Meng-eksekusi perintah SQL untuk membuat database
#db.execute("CREATE DATABASE basis_data")
# Menutup koneksi
#nagdb.close()