"""      Program to list all the files in the given directory along with their length and last modification time."""


import os
path = input("Enter the path of the file to be listed, enclosed in double quotes.\n")

dirs = os.listdir(path)
for i in dirs:
    path_n = path + "/%s" %(i)
    s = os.stat(path)
    print i +  "\t" + str(s.st_size) + "\t" + str(s.st_mtime)
