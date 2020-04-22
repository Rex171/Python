import os
import shutil
put = input('Привет! Введи путь к файлу который хочешь копировать: ')
err = os.path.exists('{}'.format(put))
if err == True:
    put2 = input('Отлично! А теперь введите путь куда будем копировать: ')
    err2 = os.path.exists('{}'.format(put2))
    if err2 == True:
        shutil.copy('{}'.format(put), '{}'.format(put2))
    else:
        print('Неправильный путь')
else:
    print('Вы ввели неправильный путь или такого не сущетсвует!{}'.format(err))