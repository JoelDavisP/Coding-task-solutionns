"""  Program to list all files in the given directory. """
import os
a= input("\nenter the path enclosed in double quotes\n")
dirs = os.listdir(a)
for i in dirs:
    print i
