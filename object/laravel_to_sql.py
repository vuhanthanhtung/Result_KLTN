from query import query


def get_query_for_sql(string):
    result=""
    ##### select 
    if ("get" or "first" or "all") in string:
        result = "select"
    return result
def get_table_name_for_sql(string):
    result=""
    if ("::" in string):
        result=string.split("::")[0]
        print result
        return result
    if ("new" in string):
        result=string.split("new")[1]
        result=result.split(")->")[0]
        return result
    return result


def Get_value_after_where(string):
    result = ""
    string=string.replace("(","")
    string=string.replace(")","")
    array=string.split(",")
    if len(array) >2 :
        result = array[0] + array[1] + array[2]
        return result
    if len(array) <= 2:
        result = array[0] + "=" + array[1]
        return result
    return result

def get_condition_for_sql(string):
    result=[]
    if ("where" in string):
        array = string.split("where")
        #if len(array) > 2:
        #    print "we will process later"
        #if len(array) <= 2:
        for i in range(1, len(array)):
            tmp=array[i].split("->")[0]
            result.append(Get_value_after_where(tmp))
    return result


### option_query: example: distinct
def get_option_query_for_sql(string):
    result=None
    if ("distinct" in string):
        result="unique"
    return result

def get_option_condition_for_sql(string):
    result=[]
    if ("where" in string):
        array=string.split("where")
        if len(array)==2:
            return None
        for i in range(1,len(array)-1):
            if ("or" in array[i].lower()):
                result.append("or")
            else:
                result.append("and")
        return result



string="(new abc)->where('lala',>,2)->orwhere('lele',3)->distinct()->get()"
query_name=get_query_for_sql(string)
table_name=get_table_name_for_sql(string)
condition=get_condition_for_sql(string)
option_query=get_option_query_for_sql(string)
option_condition=get_option_condition_for_sql(string)

abc=query(query_name,table_name,condition,option_query,option_condition)
abc.showQuery()
