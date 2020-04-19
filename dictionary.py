ListName = []
ListFamily = []
a = {'Имя' : ListName, 'Фамилия' : ListFamily}
print('Для выхода из программы введите в строку имени "Выход"')
while True:
  name = input('Введите имя: ')
  if name == "Выход":
    break
  family = input('Введите фамилию: ')
  ListName.append(name)
  ListFamily.append(family)
print(a['Имя'])
print (a['Фамилия'])
