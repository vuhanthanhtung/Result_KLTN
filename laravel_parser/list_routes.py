############### List ALL table Base on Model
import os
import glob

######################### Read all file directory 

def scan_directory(directory):
    routes_file = open("sub_folder/routes_file.txt","w+")
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
            if (( "route::get" ) in i.lower()):
                tmp = i.lower().split("route::get")[1]
                tmp = tmp.split(",")
                url = tmp[0]
                for j in tmp:
                    if "@" not in j:
                        continue
                    if "@" in j :
                        if ("=>" in j):
                            j=j.split("=>")[1]
                        if (")" not in j):
                            j=j+")"
                        if (";" in j):
                            j=j[:-2]
                    routes_file.write(url+j+"\n")
            if (( "route::post" ) in i.lower()):
                tmp = i.lower().split("route::post")[1]
                tmp = tmp.split(",")
                url = tmp[0]
                for j in tmp:
                    if "@" not in j:
                        continue
                    if "@" in j :
                        if ("=>" in j):
                            j=j.split("=>")[1]
                        if (";" in j):
                            j=j[:-2]
                    routes_file.write(url+j+"\n")


scan_directory("/root/laravel-ecommerce/routes")
