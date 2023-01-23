# fungsi 
def program():
    print ("Deret Fibonacci")
  
# fungsi rekursif dalam menentukan bilangan fibonacci
def fibonacci(n):
   if n == 0 or n == 1:
      return n
   else:
      return (fibonacci(n-1) + fibonacci(n-2))

x = int(input("Masukan Batas Deret Bilangan Fibonacci : "))
program() # memanggil Fungsi program
for i in range(x):
   print(fibonacci(i),end=' ') # Fungsi Fibonacci akan terus memanggil dirinya sendiri hingga batas x yang telah ditentukan