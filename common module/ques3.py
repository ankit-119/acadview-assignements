

import os
#files = os.listdir('C:\\Users\\A\\Desktop\\python pics')
"""commented otherwise all files will be converted into jpg and hence corroupted"""
for file in files:

    newfile = file.replace(file.split('.')[1], 'jpg')
    os.rename(file, newfile)
print(os.listdir(os.curdir))

