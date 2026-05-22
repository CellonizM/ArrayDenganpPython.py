##Implementasi hash dan pengenalan alur
class simplehashtable:
  def __init__(self,size):
    self.size=size
    self.table=[None]*size

  def hash_func(self,key):
    return hash (key) % self.size

  def insert(self, key, value):
    index = self.hash_func (key)
    self.table[index] = value

  def search (self, key):
    index = self.hash_func(key)
    return self.table[index]

#Contoh penggunaan
ht=simplehashtable(10)
ht.insert("apel",100)
ht.insert("apel",400)
ht.insert("pisang",200)


print("Nilai untuk apel : ", ht.search("apel"))
print("Nilai untuk pisang : ", ht.search("pisang"))


#Linear Probing Hash Table
class linearprobhashtable:
  def __init__(self, size):
    self.size=size
    self.table= [None] * size

  def hash_func(self, key):
    return hash(key) % self.size

  def insert(self, key, value):
    index = self.hash_func(key)
    ori_index = index

    while self.table[index] is not None:
      if self.table[index][0] == key:
        break
      index = (index + 1) % self.size
      if index == ori_index:
        raise exception(" hash table penuh")

    self.table[index]= (key, value)

  def search (self,key):
    index=self.hash_func(key)
    ori_index=index

    while self.table[index] is not None:
      if self.table[index][0] == key:
        return self.table [index][1]
      index= (index+1) % self.size
      if index == ori_index:
        break 
    return None


ht=linearprobhashtable(5)

ht.insert("A",10)
ht.insert("B",20)
ht.insert("C",30)
ht.insert("D",40)
ht.insert("E",50)

print("Nilai kunci A : ",ht.search("A"))
print("Nilai kunci B : ",ht.search("B"))
print("Nilai kunci C : ",ht.search("C"))
print("Nilai kunci D : ",ht.search("D"))
print("Nilai kunci E : ",ht.search("E"))


#Chaining Probing Hash Table
class chainhashtable:
  def __init__ (self, size):
    self.size = size
    self.table = [[] for _ in range(size)]

  def hash_func(self, key):
    return hash(key) % self.size

  def insert (self, key, value):
    index = self.hash_func(key)
    for i, (k, y) in enumerate(self.table[index]):
      if k == key:
        self.table[index][i] = (key, value)
        return
    self.table[index].append((key, value))

  def search(self, key):
    index = self.hash_func(key)
    for k, v in self.table[index]:
      if k == key:
        return v
    return None

ht = chainhashtable(3)
ht.insert("apel", 100)
ht.insert("melon", 200)
ht.insert("lemon", 300)
ht.insert("pisang", 400)

print("Nilai dari apel : ", ht.search("apel"))
print("Nilai dari melon : ", ht.search("melon"))
print("Nilai dari lemon : ", ht.search("lemon"))
print("Nilai dari pisang : ", ht.search("pisang"))

