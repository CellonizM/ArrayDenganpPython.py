##Menghapus node awal, tengah, dan akhir
##Single Linked list
#Membuat class node
class Node:
  def __init__(self, data): #setelah def dan init, gunakan 2 underscore
    self.data = data
    self.next = None #alamat node selanjutnya


class linkedlist: #class untuk storage dan mendeklarasikan saat ini head kosong
  def __init__(self):
    self.head = None

  def listprint(self): #perintah untuk menelusuri node dari awal hingga akhir
    currentnode = self.head
    while currentnode is not None:
        print(currentnode.data)
        currentnode = currentnode.next

  def addawal(self,newdata):#perintah untuk menambahkan node
    NodeB = Node(newdata)
    NodeB.next=self.head
    self.head=NodeB

  def hapusawal(self): #perintah menghapus node awal 
    afterhead = self.head
    self.head = afterhead.next

  
  def bykey(self, removekey):#perintah menghapus node melalui kunci
    head = self.head
    if(head is not None):#bagian 1
      if(head.data == removekey):
        self.head=head.next
        head=None
        return
    while(head is not None):#bagian 2
      if head.data == removekey:
        break
      prev=head
      head=head.next
    if(head==None):#bagian 3
      return
    prev.next=head.next
    head=None
    
  def delend(self): #perintah menghapus akhir node
    last = self.head
    while(last is not None):
      if last.next == None:
        break
      prev = last
      last=last.next

    if (last==None):
      return
    prev.next = last.next
    last=None

li = linkedlist()


#Menambahkan Node
li.addawal("april")
li.addawal("maret")
li.addawal("juni")
print("sebelum di remove")
li.listprint()
print("-"*30)



li.hapusawal()
print("setelah remove kunci maret")
li.listprint()

