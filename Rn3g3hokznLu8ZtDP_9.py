
def increment_string(txt):
    my_str = txt
    string = ""
    string_alpha = ""
    string_n = ""
    count = 0
    my_num = 0
    count_0 = 0
    count_n = 0
    num = 0
    for i in range (0,len(my_str)):
        if (my_str[i].isdigit()):
            string+=my_str[i]
            count+=1
        else:
            string_alpha+=my_str[i]
    #print(string)
    #print(string_alpha)
    if (len(string) > 4):
        if (string[len(string)-2] == "0"):
            num = int(string)
            num+=1
            return string_alpha+"0"+str(num)
    if (count == 0):
        my_str+="1"
        return my_str
    for i in range (0,len(string)):
        if (string[i] != "0"):
            string_n+=string[i]
        else:
            count_0+=1
            
    #print(string_n)
    for i in range (0,len(string_n)):
        if (string_n[i] == "9"):
            count_n+=1
    if (count_n == len(string_n)):
        count_0-=1
    for i in range (0,count_0):
        string_alpha+="0"
    #print(string_alpha)
    num = int(string_n)
    num+=1
    string_alpha+=str(num)
    return string_alpha
        
        
print(increment_string("foobar01002"))

