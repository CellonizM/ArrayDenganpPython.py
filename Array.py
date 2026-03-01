##ARRAY
import array as arr
a = arr.array("i",[1,2,3])
print("array baru = ",end=" ")
for i in range(0, 3):
  print(a[i], end=" ")
print()

b = arr.array("d",[2.2,4.2,3.3])
print("array baru = ",end=" ")
for i in range(0, 3):
  print(b[i], end=" ")
print()

a = arr.array("i",[1,2,3])
print("array baru = ",*a)
b = arr.array("d",[2.2,4.2,3.3])
print("array baru = ",*b)

#Menambahkan elemen ke array
import array as arr
a= arr.array("i",[1,2,3,4])
print("array awal = ", end=" ")
for i in range(0,4):
  print(a[i], end=" ")
print()

a.insert(5,6) #indeks dan value nya
print("array setelah dimasukkan data baru =",end=" ")
for i in a:
  print (i, end=" ")
print()

a.append(7)
print("array setelah diappend =",end=" ")
for i in a:
  print(i,end=" ")


#Mengangkes elemen array
import array as arr
a= arr.array("i",[1,2,3,4])
print("elemen yang diakses = ",a[3])
print("elemen yang diakses = ",a[0])
print()

b = arr.array("d",[2.2,4.2,3.3])
print("elemen yang diakses = ",b[2])
print("elemen yang diakses = ",b[0])


#Menghapus elemen array
import array as arr
a = arr.array("i",[1,2,3,4,5,6])
print("Array yang asli =",end=" ")
for i in range(0,6):
  print(a[i], end=" ")
print()

print("elemen yang di pop = ",end="")
print(a.pop(2))
print("array setelah di pop = ",end=" ")
for i in range(0,5):
  print(a[i],end=" ") #angka 3 menghilang dari array
print()

a.remove(4)
print("array setelah diremove",*a)

#Memotong elemen array
import array as arr
L = [1,2,3,4,5,6,7,8,9,10]
a = arr.array("i",L)
print("array asli =")
for i in (a):
  print(i,end=" ")
print()

potong_dari = a[3:6]
print("array setelah dipotong dari indeks 3-6 =")
print(*potong_dari)
potong_mulai = a[2:]
print("array setelah dipotong dari indeks ke 2 =")
print(*potong_mulai)
potong = a[:]
print("array setelah dipotong semua elemen nya")
print(*potong)

#Mengubah elemen array
import array as arr
a = arr.array("i",[1,5,3,4,2,1])
print("array setelah dirubah= ",end=" ")
for i in range(0,6):
  print(a[i], end=" ")
print()

a[2] = 6 #mengubah indeks ke 2
print("array setelah dirubah= ",end=" ")
for i in range(0,6):
  print(a[i], end=" ")
print()
a[5] = 4 #mengubah indeks ke 5 menjadi 4
print("array setelah dirubah= ",end=" ")
for i in range(0,6):
  print(a[i], end=" ")


#Operasi dalam array
import array as arr
a=arr.array("i",[1,2,3,4,5,6,2,5])
#Menghitung elemen array
hitung =a.count(5)
print("banyak angka 5 dalam array = ", hitung)

#Membalik elemn array
print("array asli =",*a)
a.reverse()
print("array setelah dibalik = ",*a)


#Meng-extend elemen array
import array as arr
a = arr.array("i",[1,2,3,4,5,6])
print("Array yang asli =",*a)
a.extend([7,8,9,10,11])
print("array setelah di extend= ",*a)
