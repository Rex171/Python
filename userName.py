import getpass
import os
a = getpass.getuser()
#directory = 'C:/Users/'+a
#files = os.listdir(directory) 
print(a)
#получение древа каталогов
for i in os.listdir('/Users/'+a):
    print(i)
#получение директории
dir = os.path.abspath(os.curdir)
print('Текущий пользователь: ' + a)
print('Абсолютный путь к дериктории в которой запущен скрипт: '+dir)