import os
import re
def lower_string(string):
    return string.lower()

def scan_select(string):
    result=""
    string=lower_string(string)
    if ("\"select" in string):
        tmp_str1=string.split("\"select")[1]
#        tmp_str2=string.split("\";")[1]
        tmp_str=tmp_str1.split("\"")[0]
        tmp_str="select"+tmp_str
        result=tmp_str
#        if(tmp_str2==""):
#            return result
#        tmp=scan_select(tmp_str2)
#        result.append(tmp)
    if ("\'select" in string):
        tmp_str1=string.split("\'select")[1]
        tmp_str=tmp_str1.split("\'")[0]
        tmp_str="select"+tmp_str
        result=tmp_str
    return result

def scan_insert(string):
    result=""
    string=lower_string(string)
    if("\"insert" in string):
        tmp_str1=string.split("\"insert")[1]
        tmp_str=tmp_str1.split("\"")[0]
        tmp_str="insert"+tmp_str
        result=tmp_str
    if ("\'insert" in string):
        tmp_str1=string.split("\'insert")[1]
        tmp_str=tmp_str1.split("\'")[0]
        tmp_str="insert"+tmp_str
        result=tmp_str
    return result

def scan_update(string):
    result=""
    string=lower_string(string)
    if("\"update" in string):
        tmp_str1=string.split("\"update")[1]
        tmp_str=tmp_str1.split("\"")[0]
        tmp_str="update"+tmp_str
        result=tmp_str
    if ("\'update" in string):
        tmp_str1=string.split("\'update")[1]
        tmp_str=tmp_str1.split("\'")[0]
        tmp_str="update"+tmp_str
        result=tmp_str
    return result

def Del_space(string):
    return string.strip()

def Del_all_space(string):
    return string.replace(" ","")

def Replace_spaces_to_1_space(string):
    while ("  " in string):
        string=string.replace("  "," ")
    return string

def split_multi_query(string):
    return Del_space(string).split(";")

def Del_comment(string):   
    result=""
    string=Replace_spaces_to_1_space(string)
    if "//" in Del_space(string)[0:2]:
        return result
    if "; //" in string:
        string=string.split("; //")[0]
        result=string+";"
        return result

    if ";//" in Del_space(string):
        string=string.split(";//")[0]
        result=string+";"
        return result
    return string

def Del_block_comment(string):
        if ("/*" in string) and ("*/" in string):
            string=""
        return string
def Del_html(string):
    result=""
    a=Del_all_space(string)
    if (a[0]=="<"):
        return result
    return string

def check_sub_comma(string):
    flag=0
    string=Del_space(string)
#    if (string[-1]!=";") and (string[-1] != "*/"):
    if (string[-1]!=";") and (("public function" not in string) and ("*/" not in string)):
        flag=1
    return flag

def check_kep_don(string):
    flag=0
    if ( "})" in string.strip()):
        flag=1
    return flag


def Del_kep(string):
    result = "0"
    #string= Del_all_space(string)
    #string= string.replace("\n","")
    #string=string.replace("\t","")
    #string=string.replace("\r","")
    #string=string.replace(" ","")
    #if (Del_all_space(string) == "{") or (Del_all_space(string) == "}"):
    #    result = "1"
    if ("})" in string):
        result="0"
        return result

    if ("{" in string) or ("}" in string):
        result = "1"
    return result

#string="           zyx=\"select * from abc\" abc=\"select * from abc\"             "
#string="    abc=\"     select * from avxc \"          ;        "
#a=split_multi_query(string)
#print a
    
#result=Del_space(string)
#print result
#result=[]
#save =""
#f = open("/var/www/html/basicwebsite/info.php","r").readlines()
#f = open("/opt/script/test1.txt","r").readlines()
#for i in f:
#    if (Del_space(i) ==""):
#        continue
##### Remove all comment
#    tmp=Del_comment(i)
#    if (tmp == ""):
#        continue
#    else:
#        i=tmp
##### Remove all HTML line
#    tmp=Del_html(i)
#    if (tmp == ""):
#        continue
#    else:
#        i=tmp
###### 
#    if (check_sub_comma(i)==1):
#        save=save + " " +Del_space(i).replace("\n"," ")
#        print save
#        continue
#    else:
#        save=save + " " +Del_space(i).replace("\n"," ")
#    print save
#    if (save!=""):
#        array = split_multi_query(save) 
#    if (len(array)!=1):
#        for j in array:
#            if (j!=""):
#                ####### solve the problem space in string such as abc=" select/insert/update fdsfsdfsdf";
#                j=Replace_spaces_to_1_space(j)
#                if ("\" " in j):
#                    j=j.replace("\" ","\"")
#                if ("\' " in j):
#                    j=j.replace("\' ","\'")
#                j=Del_space(j);
#                if(scan_select(j)!= ""):
#                    result.append(scan_select(j))
#                if(scan_insert(j)!= ""):
#                    result.append(scan_insert(j))
#                if(scan_update(j)!= ""):
#                    result.append(scan_update(j))
#    save=""
#print result
        
