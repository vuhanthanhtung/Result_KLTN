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

string="(new abc)->where('lala',>,2)->orwhere('lele',3)->get()"
result=get_option_condition_for_sql(string)
print result

