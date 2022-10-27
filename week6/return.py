# fungsi return
def volume_batubata(luas, tinggi):
    return luas * tinggi 
print ("volume batu bata adalah :  ", volume_batubata(15, 5))   


# fungsi 2 return
def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)

  return bilangan

hasil = hitung_pangkat(4, 3)
## print(f'Hasil = {hasil}')  
print(" Hasil dari 4 pangkat 3 : ", hasil)