
# Hello World program in Python
    
def fib_str(n, txt):
    my_word = ""
    my_list = []
    my_list.append(txt[0])
    my_list.append(txt[1])
    my_word+=txt[0]+","+" "+txt[1]
    if (n == 2):
        my_word = txt[0]+","+" "+txt[1]
        return my_word
    elif (n>2):
        for i in range (2,n):
            my_list.append(my_list[i-1]+my_list[i-2])
    for i in range (2,len(my_list)):
        my_word+=","+" "+my_list[i]
    return my_word
txt = ["n","k"]
print(fib_str(6,txt))

