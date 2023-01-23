import mysql.connector
import os

nagdb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="password",
  port=3306,
  database="crud"
)
cursor = nagdb.cursor()
sql = """CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")

def insert_data(nagdb):
  name = input("Masukan nama: ")
  address = input("Masukan alamat: ")
  val = (name, address)
  cursor = nagdb.cursor()
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  cursor.execute(sql, val)
  nagdb.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(nagdb):
  cursor = nagdb.cursor()
  sql = "SELECT * FROM customers"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(nagdb):
  cursor = nagdb.cursor()
  show_data(nagdb)
  customer_id = input("pilih id customer> ")
  name = input("Nama baru: ")
  address = input("Alamat baru: ")

  sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
  val = (name, address, customer_id)
  cursor.execute(sql, val)
  nagdb.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(nagdb):
  cursor = nagdb.cursor()
  show_data(nagdb)
  customer_id = input("pilih id customer> ")
  sql = "DELETE FROM customers WHERE customer_id=%s"
  val = (customer_id,)
  cursor.execute(sql, val)
  nagdb.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(nagdb):
  cursor = nagdb.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(nagdb):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(nagdb)
  elif menu == "2":
    show_data(nagdb)
  elif menu == "3":
    update_data(nagdb)
  elif menu == "4":
    delete_data(nagdb)
  elif menu == "5":
    search_data(nagdb)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(nagdb)