# looping for 
bilangan = [1,2,3,4,5]
for x in bilangan:
    print(x)
#for 
kota = ["Bali", "Yogya", "Bandung"]
for wisata in kota:
    print ("Saya suka wisata di ", wisata)

# looping While
count = 0
while (count < 9):
    print ("The count is: ", count)
    count = count + 1


# looping with range
for var in range(3):
    print (var)

# looping with continue & break
for a in "pemograman":
    if a=="p":
        continue
    if a=="g":
        #continue
        break
    print (a)
print("end")
a = "pemograman"
print(len(a))

# Nested Loop
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, " adalah bilangan prima")
    i = i + 1
#nestedloop2
listKota = [
  'Jakarta', 'Surabaya', 'Makassar'
]
for kota in listKota:
  print(kota)
  listTempat = [
    'Taman', 'Lapangan', 'Mall'
  ]
  while listTempat:
    print('-->', listTempat.pop(0))
#nestedloop3
for i in range(3):
  print('Puluhan dalam bentuk [i] = ', i)
  for j in range(5):
    print('     Satuan dalam bentuk [i, j] = ', str(i) + ', ' + str(j))
