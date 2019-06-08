import os

def get_url_from_route(string):
    url=""
    tmp = string.split(" ")
    url = tmp[0].replace("(", "")
    url = url.replace("'", "")
    return  url

def get_controller_function_name(string):
    controller_function_name="" 
    tmp = string.split(" ")
    controller_function_name = tmp[1].split("')")[0]
    controller_function_name = controller_function_name.replace("'", "")
    return controller_function_name

def get_controller_name(string):
    controller_name=""
    tmp = string.split("@")
    controller_name = tmp[0]
    if ("\\" in controller_name) or ("/" in controller_name):
        controller_name = controller_name.split("\\")[-1]
    return controller_name

def get_function_name(string):
    function_name=""
    tmp = string.split("@")
    function_name = tmp[1]
    return function_name

def get_all_query_in_controller_function_file(directory,string):
    result=[]
    array = open(directory,"r").readlines()
    for i in range(0,len(array)):
        if (string in array[i]):
            j=i+1
            if (j < len(array)):
                for j in range(j,len(array)):
                    if ("public function" not in array[j]):
                        result.append(array[j])
                    else:
                        break
    return result

def write_files(directory,array):
    write_files = open(directory,"w+")
    for i in array:
        write_files.write(i)
def Process_Url_Query():
    directory="sub_folder"
    files="sub_folder/routes_file.txt"
    lines=open(files,"r").readlines()
    for i in lines:
        url = get_url_from_route(i)
        controller_function_name = get_controller_function_name(i)
        controller_name = get_controller_name(controller_function_name)
        function_name = get_function_name(controller_function_name)
        files_1= directory + "/controller/" + controller_name +".txt"
        files_2= directory + "/result/" + url + ".txt"
        write_files = open(files_2,"w+")
        read_files = open(files_1,"r")
        query = get_all_query_in_controller_function_file(files_1,string)
        write_files(files_2,query) 

    
#Process_Url_Query()

#print get_url_from_route("('/home' 'homecontroller@index')->name('home')")
#a = get_controller_function_name("('/home' 'lala/auth/homecontroller@index')->name('home')")
#print get_controller_name(a)
#print get_function_name(a)
files=open("test.txt","r").readlines()
query=get_all_query_in_controller_function_file("test.txt","vuongcc")
write_files("test_write.txt",query)
