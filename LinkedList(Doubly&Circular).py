##Doubly Node 
#Menyisipkan dan menghapus tengah
class Node:
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next =None
n1=Node("jakarta")
n2=Node("paris")
n3=Node("jerman")

class Dll:
  def __init__(self):
    self.head=None

  def sisiptengah (self,pos,newdata):
    n=Node(newdata)
    temp=self.head
    for i in range(1,pos-1):
      temp=temp.next
    n.prev=temp
    n.next=temp.next
    temp.next.prev=n
    temp.next=n

  def hapuskey(self,pos):
    temp=self.head.next
    before=self.head
    for i in range(1,pos-1):
      temp=temp.next
      before=before.next
    before.next=temp.next
    temp.next.prev=before
    temp.next=None
    temp.prev=None

  def display(self):
    if self.head is None:
      print("double linked list kosong")
    else:
      temp=self.head
      while temp is not None:
        print(temp.data, "<->", end=" ")
        temp=temp.next


L=Dll()
L.head=n1
L.head.next=n2
n2.prev= L.head
n2.next=n3
n3.prev=n2

L.sisiptengah(3,tengah)
L.hapuskey(2)
L.display()
print("null")




##Circular Node
#Menyisipkan dan menghapus node akhir
class Node:
  def __init__(self,data):# def __init__(node1/2/3,nilainya)
    self.data=data
    self.next=None

n1=Node("jeruk")
n2=Node("apple")
n3=Node("semangka")

class Circular:
  def __init__(self):
    self.head=None#Node awal
    self.tail=None#Node terakhir
  
  def sisipakhir(self,x):
    new = Node(x)
    if self.head is None:
      self.head=new
      self.tail=new
      self.tail.next=self.head
    else:
      self.tail.next=new
      self.tail=new
      self.tail.next=self.head

  def hapusakhir(self):
    if self.head is None:
      print("node tidak ada")
    else:
      if self.head==self.tail:
        self.head=None
      else:
          temp=self.head
          while temp.next != self.tail:
            temp=temp.next
          self.tail=None
          self.tail=temp
          temp.next=self.head
      

  def display(self):
    if self.head is None:
      print("Node kosong")
    else:
      temp=self.head
      print(temp.data,"-->",end=" ")
      while temp.next != self.head:
        temp=temp.next
        print(temp.data,"-->",end=" ")
      print(temp.next.data)


C=Circular()

C.head=n1 #Menjadikan n1 sebagai head
C.tail=n1 #Menjadikan n1 sebagai tail
C.tail.next=C.head #head dihubungkan dengan tail

C.tail.next=n2 #alamat dari tail (n1) = n2
C.tail=n2 #Menjadikan n2 sebagai tail
C.tail.next=C.head #Head dihubungkan dengan tail

C.tail.next=n3 #alamat dari tail (n2)=n3
C.tail=n3 #Menjadikan n3 sebagai tail
C.tail.next=C.head #head dihubungkan dengan tail

C.sisipakhir()
C.hapuskahir()
C.display()


