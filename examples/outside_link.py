#import ../laravel_parser/scan
import os
import glob
def read_file_name_in_directory(directory):
    listfile=[]
    for r,d,f in os.walk(directory):
        for files in f:
            if ".php" in files:
                listfile.append(os.path.join(r,files))
    return listfile

def get_function(string):
    result = ""
    if ( "public function" in string ):
        result = string
    return result

def process_in_model_file_directory(model_name,function_name):
    array=[]
    model_name=model_name +".php"
    model_file="models/"+model_name
    model_file=open(model_file,"r").readlines()
    for i in range(0,len(model_file)):
        if (model_file[i].strip()=="#"):
            j=i+1
            
            if (j < len(model_file)) and (function_name.strip() in model_file[j].strip()) :
                z=i+2
                while (z < len(model_file)) and (model_file[z].strip() !="#"):
                    array.append(model_file[z])
                    z=z+1


    return array            
    






    

def Moving():
    result=""
    model_function = open("model_function","r").readlines()
    controller_file = open("controller.php","r").readlines()
    model_file_directory = "models"
    for i in controller_file:
        if ("public function" in i):
            print i.strip()
            continue
        for j in model_function:
            if (j.strip() in i.strip()):
                
                model_name=j.split("->")[0]
                model_name=model_name[5:-1]
                function_name=j.split("->")[1]
               # print model_name.strip()
               # print function_name.strip()
                print process_in_model_file_directory(model_name,function_name)
Moving()
