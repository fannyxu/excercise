#!/usr/bin/python
#Filename: print_largefile.py

import os,sys

def isLarge(file_path):
    Bigjudge = 2000000
    filesize = os.path.getsize(file_path)
    if os.path.isfile(file_path) == False:
        raise os.error("There is no this file")
    if(filesize > Bigjudge):
        return filesize
    else:
        return 0
def getAlltree(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path,name)
        if os.path.isfile(full_path):
            filesize = isLarge(full_path)
            if filesize > 0:
                print("FilePath%s     FileSize%d"%(full_path,filesize))
        if os.path.isdir(full_path):
            getAlltree(full_path)
def main():
    dir_path = r"F:\accumulate"
    getAlltree(dir_path)
    print("Search Over")

main()
