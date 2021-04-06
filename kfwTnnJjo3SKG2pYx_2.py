
def replace_nums(string):
    newstring,num = "",""
    for index,i in enumerate(string):
        if not i.isdigit():
            if num != "":
                newstring += bin(int(num))[2:]
                num = ""
            newstring += i
        else:num += i
    return newstring

