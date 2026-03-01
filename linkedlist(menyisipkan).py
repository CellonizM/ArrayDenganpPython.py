##Membuat Linked List
#Membuat class node
class Node:
  def __init__(self, data): #setelah def dan init, gunakan 2 underscore
    self.data = data
    self.next = None #alamat node selanjutnya


n1=Node("januari")
n2=Node("februari")
n3=Node("maret")

class linkedlist: #class untuk storage dan mendeklarasikan saat ini head kosong
  def __init__(self):
    self.head = None
    
  def sisipawal(self,newdata):#perintah untuk menyisipkan data baru diawal
    NodeB = node(newdata)
    NodeB.next = self.head
    self.head = NodeB

  def sisiptengah(self,node_mid,newdata):#perintah untuk menyisipkan data baru diawal
    if node_mid is None:
      print("node yang dipanggil tidak ada")
      return
    NodeB = Node(newdata)
    NodeB.next = node_mid.next
    node_mid.next = NodeB

   def sisipakhir(self,newdata):#perintah untuk menyisipkan data baru diawal
    NodeB = Node(newdata)
    if self.head is None:
      self.head = NodeB
      return
    last=self.head
    while(last.next):
      last=last.next
    last.next=NodeB
     

    
  def listprint(self): #perintah untuk menelusuri node dari awal hingga akhir
    currentnode = self.head
    while currentnode is not None:
        print(currentnode.data,"->",end=" ")
        currentnode = currentnode.next

li = linkedlist()
li.head=n1

n1.next = n2 #menghubungkan antar node
n2.next = n3


li.listprint()
print("null")
