import scan
import os
import glob

def get_function(string):
    result = ""
    if ( "public function" in string ):
        result = string
    if ( "public static function" in string ):
        result = string
    return result

def get_query(string):
    result=""
    model_file = open("sub_folder/model_files.txt","r")
    model_file = model_file.readlines()
    for i in range(0,len(model_file)):
        model_file[i]=model_file[i].replace("\n","")
    for i in model_file:
        tmp= i+"::"
        if (tmp in string):
            result= string
        tmp= "new "+i
        if (tmp in string):
            result= string
        if "$query->" in string:
            result = string
        if "this->" in string:
            result = string
	if "self::" in string:
	    result = string
    return result

def scan_directory(directory):
    listfile = []
    for r,d,f in os.walk(directory):
        for files in f:
            if ".php" in files:
                listfile.append(os.path.join(r,files))
    return listfile

#file_directory="/root/Desktop/laravel-ecommerce/app/Models/CmsCategory.php"
directory="/root/laravel-ecommerce"
model_listfile = scan_directory(directory)
for files in model_listfile:
	flag=0
	f = open(files, "r")
#	print f.name
	lines = f.readlines()
	for i in lines:
	    if "extends model" in i.lower():
		flag = 1
		break
	if flag == 1:
		print f.name
		for i in lines:
		    string = ""
		    if (scan.Del_space(i) ==""):
		       	continue
		    if (scan.Del_kep(i) == "1"):
		        continue
		    tmp=scan.Del_comment(i)
		    if (tmp == ""):
		        continue
		    else:
		        i=tmp
		    tmp=scan.Del_html(i)
		    if (tmp == ""):
		        continue
		    else:
		        i=tmp
		    if (scan.check_sub_comma(i)==1):
		        string=string + " " +scan.Del_space(i).replace("\n"," ")
		        continue
		    else:
		        string=string + " " +scan.Del_space(i).replace("\n"," ")
		    result=""
		    result=get_function(string)
		    if (result != ""):
		        print result
		    result=get_query(string)
		    if (result != ""):
		        print result

