
def addBinary(a,b):
  for ch in a: assert ch in {'0','1'}, 'не верные числа'+ ch
  for ch in b: assert ch in {'0','1'}, 'не верные числа'+ ch
  sumx = int(a, 2) + int(b, 2)
  return bin(sumx)[2:]
def minusBinary(a,b):
  for ch in a: assert ch in {'0','1'}, 'не верные числа'+ ch
  for ch in b: assert ch in {'0','1'}, 'не верные числа'+ ch
  minx = int(a, 2) - int(b, 2)
  return bin(minx)[2:]
def multiBinary(a,b):
  for ch in a: assert ch in {'0','1'}, 'не верные числа'+ ch
  for ch in b: assert ch in {'0','1'}, 'не верные числа'+ ch
  mulx = int(a, 2) * int(b, 2)
  return bin(mulx)[2:]
def delBinary(a,b):
  for ch in a: assert ch in {'0','1'}, 'не верные числа'+ ch
  for ch in b: assert ch in {'0','1'}, 'не верные числа'+ ch
  delx = int(a, 2) - int(b, 2)
  return bin(delx)[2:]

a = input("Введите 1 число: ")
b = input("Введите 2 число: ")

d = addBinary(a,b)
d1 = minusBinary(a,b)
d2 = multiBinary(a,b)
d3 = delBinary(a,b)
print(d,d1,d2,d3)
