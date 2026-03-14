##Program Queue
#Queue dengan list
print("Ini adalah queue dengan list")
queue = [ ]

queue.append("a")
queue.append("i")
queue.append("u")
queue.append("e")
queue.append("o")


print("\nisi dari stack awal")
print(*queue)

#gunakan pop(0) agar yang dihapus didalam queue menjadi FIFO
print("\nelement yang di pop dengan prinsip fifo")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nisi dari stack setelah di pop")
print(*queue)

#Queue dengan deque
print("Ini adalah queue dengan collections.deque")
from collections import deque
queue = deque()

#Menambahkan elemen menggunakan fungsi append()
queue.append("a")
queue.append("i")
queue.append("u")
queue.append("e")
queue.append("o")


print("\nisi dari stack awal")
print(*queue)

#Menghapus elemen dengan prinsip FIFO menggunakan fungsi popleft()
print("\nelement yang di pop")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print("\nisi dari stack setelah di pop")
print(*queue)

#Queue dengan import queue
print("Ini adalah queue dengan queue.queue")
from queue import Queue #memanggil library
qu = Queue(maxsize=5) #menetapkan banyak elemen dalam queue
print(qu.qsize())

qu.put("a") #Menambahkan elemen dengan perintah put()
qu.put("i")
qu.put("u")
qu.put("e")
qu.put("o")

print("Full = ",qu.full()) #Mengecek apakah data penuh atau tidak
print("Size = ",qu.qsize()) #Mengecek apakah jumlah data sama dengan deklarasi

print("\nElemen yang di dequeue")
print(qu.get()) #Menghapus elemen dengan perintah get()
print(qu.get())
print(qu.get())
print("\nEmpty = ",qu.empty())
print("Full = ",qu.full())


#Queue dengan single linked list
print("Ini adalah queue dengan linked list")
class queue: #Membuat class queue
  def __init__ (self):
    self.queue=list() #Menjadikan elemen queue sebagai list

  def addtoqu(self,data): #Membuat fungsi menambahkan element
    if data not in self.queue:
      self.queue.insert(0,data)
      return True
    return False

  def remove(self): #Membuat fungsi menghapus elemen
    if len(self.queue)>0:
      return self.queue.pop()
    return("Tidak ada elemen di queue")

  def size(self): #Membuat fungsi menghitung jumlah elemen
    return len(self.queue)

qu = queue()
print(qu.addtoqu("Jan"))
print(qu.addtoqu("Feb"))
print(qu.addtoqu("Mar"))
print(qu.addtoqu("Apr"))
print(qu.size())
print(qu.remove())
print(qu.remove())
print(qu.size())
print(qu.addtoqu("Apr"))

