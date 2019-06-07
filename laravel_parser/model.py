############### List ALL table Base on Model
import os
import glob

######################### Read all file directory 

def scan_directory(directory):
    model_files= open("sub_folder/model_files.txt","w+")
    listfile = []
    Result = 0
    for r,d,f in os.walk(directory):
        for files in f:
            if ".php" in files:
                listfile.append(os.path.join(r,files))
    print listfile
    for files in listfile:
        f = open(files,"r")
        f = f.readlines()
        for i in f:
            if ( "extends model" in i.lower()):
                tmp=i.split(" ")
                model_files.write(tmp[1]+"\n")


scan_directory("/root")
