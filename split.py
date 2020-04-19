a = input('Введите числа через пробел: ').split()
print(a)
b = input('Введите число для поиска в массиве: ')
count = 0
for i in range(len(a)):
  if a[i] == b:
    count+=1
print('Указанное число встречается в массиве '+str(count) + ' раз(-а)')