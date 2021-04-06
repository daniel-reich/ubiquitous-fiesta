
def valid_name(name):
    # count is word counter
    count = len(name.split())
    # storage for words
    flag = ""
    s1 = ""
    s2 = ""
    s3 = ""
    if count > 3 or count < 2:
        return False
    # splitting words to be analized individualy
    s1 = name.split()[0]
    s2 = name.split()[1]
    # checks is word is initial and if so one
    def initial_check(inp):
        if(len(inp)) == 2:
            if(inp[0].isupper()):
                if(inp[1] != '.'):
                   return False
                else:
                    return True
            else:
                return False
    # checks is word is name and if so one
    def name_check(inp):
        if(len(inp)) > 2:
            if(inp[0].isupper()):
                return True
            else:
                return False
        else:
            return False
    # 2 words check
    if count == 2:
        if(initial_check(s1)):
            flag += "i"
        if(name_check(s1)):
            flag += "n"
        if(initial_check(s2)):
            flag += "i"
        if(name_check(s2)):
            flag += "n"
    if(flag) == "in":
        return True
    elif(count == 2):
        return False
​
    # 3 words check
    if count == 3:
        s3 = name.split()[2]
        if(initial_check(s1)):
            flag += "i"
        if(name_check(s1)):
            flag += "n"
        if(initial_check(s2)):
            flag += "i"
        if(name_check(s2)):
            flag += "n"
        if(initial_check(s3)):
            flag += "i"
        if(name_check(s3)):
            flag += "n"
​
    if(flag == "nin" or flag == "nnn" or flag == "iin"):
        return True
    elif(count == 3):
        return False

