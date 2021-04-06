
def countdown(n, txt):
    count_list = []
    number = 0
    message = " "
​
    for i in range(n):
        number = (n - i) 
        count_list.append(str(number) + ".")
​
    txt = txt.upper()
    count_list.append(txt + "!")
​
    return(message.join(count_list))

