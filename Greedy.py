#Coin Change
def coin_change_greedy(amount, coins):
  coins.sort(reverse=True)
  result = []
  for coin in coins:
    while amount >= coin:
      amount -= coin
      result.append(coin)
  return(result)

#Penerapan
amount = 57
coins = [25, 10, 5, 1]
change= coin_change_greedy(amount, coins)
print(" Koin yang digunakan = ",change)
#-----------------------------------------------------------------------------------

##Fractional Knapsack
def fractional_knapsack(items, capacity):
  #items = list of tuples (value, weight)
  items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
  total_value = 0.0
  for value, weight in items:
    if capacity >= weight:
      capacity -= weight
      total_value += value
    else:
      total_value += value * (capacity / weight)
      break
  return total_value
#Contoh penggunaan
items =[(60,10), (100,20),(120,30)] #nilai dan berat didalam list
capacity = 50
max_value= fractional_knapsack(items, capacity)
print("Nilai maks yang dapat dibawa : ",max_value)
#-----------------------------------------------------------------------------------

##Minimum Spanning Tree : Prim dan Kruskal
#Contoh kode program 1
import heapq

def prim_mst(graph, start):
  visited = set()
  min_heap =[(0, start)]
  total_weight = 0

  while min_heap:
    weight, node = heapq.heappop(min_heap)
    if node in visited:
      continue
    visited.add(node)
    total_weight += weight
    for neighbor, edge_weight in graph [node]:
      if neighbor not in visited:
        heapq.heappush(min_heap, (edge_weight, neighbor))
  return total_weight

#Representasi graf : adjecency list
graph = {
    'A':[('B',2), ('C',3)],
    'B':[('A',2), ('C',1), ('D',1)],
    'C':[('A',3), ('B',1), ('D',4)],
    'D':[('B',1), ('C',4)]
}

print("Total bobot MST (Prim): ", prim_mst(graph,'A'))
#-----------------------------------------------------------------------------------

#Contoh kode program 2
def kruskal_mst(edges, n_nodes):
  parent = {i: i for i in range (n_nodes)}

  def find(x):
    while parent[x] != x:
      x = parent[x]
    return x

  def union (x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
      parent[root_y] = root_x
      return True
    return False

  edges.sort(key=lambda x: x[2])
  total_weight = 0
  for u, v, weight in edges :
    if union(u, v):
      total_weight += weight
  return total_weight

#edges: (node1 (awal), node2(tujuan), weight ), node bertipe data integer
edges = [(0, 1, 2), (0, 2, 3), (1, 2, 1), (1, 3, 1), (2, 3, 4)]
print('Total bobot MST(Kruskal): ',kruskal_mst(edges,4))
