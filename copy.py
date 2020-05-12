import os
import shutil
put = input('Введите путь к файлу который хотите скопировать: ')
err = os.path.exists('{}'.format(put))
if err == True:
    put2 = input('Введите путь куда копировать: ')
    err2 = os.path.exists('{}'.format(put2))
    if err2 == True:
        shutil.copy('{}'.format(put), '{}'.format(put2))
    else:
        print('Неправильный путь')
else:
    print('Вы ввели неправильный путь или такого не сущетсвует!{}'.format(err))    print('Вы ввели неправильный путь или такого не сущетсвует!')