# импортирует функции для манипулирования времени и дат
import datetime
# просим пользователя ввести даты что бы определить разницу во времени
data1 = input('Введите 1 дату (гггг-мм-дд): ')
data2 = input('Введите 2 дату (гггг-мм-дд): ')
# разделяем дату через сплит, на части
a1 = data1.split('-')
b1 = data2.split('-')
# через функцию datetime можно будет выяснить разницу во времени, между этими датами
a3 = datetime.datetime(int(a1[0]),int(a1[1]),int(a1[2]))
b3 = datetime.datetime(int(b1[0]),int(b1[1]),int(b1[2]))
# создаем переменую которая возращает разницу
sum = abs(a3-b3)
# выводим ответ
print(sum)