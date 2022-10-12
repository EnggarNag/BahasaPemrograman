#kondisi Nested IF dalam menentukan predikat nilai
nilai = int(input('Masukkan nilai: '))

if (nilai <= 100):
   print ("Nilai A")
   if (nilai <= 80):
      print ("NIlai B")
   elif (nilai <= 60):
      print ("Nilai C")
   elif (nilai <= 40):
      print ("Nilai D")
   elif (nilai <= 20):
      print ("Nilai E")
else:
   print ("Nilai tidak bisa melebihi 100")

print ("Terima Kasih")