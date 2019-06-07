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

def get_all_query_from_function(function_name,model_file):
    array=[]
    file_process=open(model_file,"r").readlines()
    for i in range(0,len(file_process)):
        if (file_process[i].strip()=="#"):
            j=i+1

            if (j < len(file_process)) and (function_name.strip() in file_process[j].strip()) :
                z=i+2
                while (z < len(file_process)) and (file_process[z].strip() !="#"):
                    array.append(file_process[z])
                    z=z+1
    return array

def get_value(string):
    result=[]
    if ( "(" in string) and (")" in string):
        string=string.split("(")[1]
        string=string.split(")")[0]
        result=string.split(",")
    return result

def get_array_variable(model_function_query_file,function_name):
    result=[]
    file_process=open(model_function_query_file,"r").readlines()
    for i in range(0,len(file_process)):
        if (file_process[i].strip()=="#"):
            j=i+1
            if (j < len(file_process)) and (file_process[j].strip()!="#"):
                if ( function_name in file_process[j]):
                    result=file_process[j]
                    return result
    return result

def replace_variables_to_values(array_variable,array_value,array_query):
    result=[]
    if (array_variable == []):
        result = array_query
        return result

    if (array_value == []):
        result = array_query
        return result

    for i in array_query:
        tmp = i
        for j in range(0,len(array_variable)):
            if ("$"+array_variable[j] in i):
                tmp=tmp.replace("$"+array_variable[j],array_value[j])
        result.append(tmp)
    return result

def transfer(model_function_query_file):
    file_process=open(model_function_query_file,"r").readlines()
    for i in range(0,len(file_process)):
  #      if (file_process[i].strip()=="#"):
  #          j=i+1
  #          if (j < len(file_process)) and (file_process[j].strip()!="#"):
  #              array_variable=get_value(file_process[j].strip())
  #              print array_variable
        if ("this->" in file_process[i].strip()):
            function_name=file_process[i].strip().split("->")[1]
            array_value=function_name
            function_name=function_name.strip().split("(")[0]
            array_variable=get_array_variable(model_function_query_file,function_name)
            array_variable=get_value(array_variable)
            array_value=get_value(array_value)
            array_query = get_all_query_from_function(function_name,model_function_query_file)
            b = replace_variables_to_values(array_variable,array_value,array_query)
            print b
        else:
            print file_process[i]

transfer("/opt/examples/models/Apple.php")
#print get_all_query_from_function("iphone","/opt/examples/models/Apple.php")

