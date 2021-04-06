
def format_phone_number(lst):
    a = ""
    a1 = lst[:3]
    a2 = lst[3:6]
    a3 = lst[6:]
    for i in a1:
        a = a + str(i)
    a = '(' + a + ')' + ' '
    for i in a2:
        a = a+str(i)
    a = a+'-'
    for i in a3:
        a = a+str(i)
    
    return a

