def Del_html(string):
    result=""
    a=string.replace(" ","")
    if a[0]=="<":
        return result
    return string


a="           <                fdsfdsfsdfsdfsdfsdfsdfsdf"
b=Del_html(a)
print b
