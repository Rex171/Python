import getpass
import os
a = getpass.getuser()
directory = 'C:/Users/'+a
files = os.listdir(directory) 
print(a)
print(os.getcwd)