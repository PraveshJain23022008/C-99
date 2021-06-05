import os

#to create a new folder/directory
os.mkdir("\C-99\FolderA")
#check the current directory
os.getcwd()
#checking the specified path exists or not
path='..\C-98\function.py'
exsist=os.path.exists(path)
print(exsist)
#split path and Root and ext
path1="C:\Users\itsam\Desktop\Python Projects\C97\test.py"
root_ext=os.path.splitext(path1)
#print root and ext
print("root part:",root_ext[0])
print("ext part:",root_ext[1],"\n")
#to get folder lists
os.listdir()
#shutil is used to move or copy files and directory
import shutil
shutil.move( source,destination)
shutil.copy()