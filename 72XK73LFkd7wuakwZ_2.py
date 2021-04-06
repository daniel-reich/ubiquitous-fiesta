
def junction_or_self(ognumber):
    junction_list = []
    junction_list2 = []
    index = -1
    
    for i in range (0, ognumber):
        test_number = ''
        test_number = str(i)
        add_number = 0
        for x in range(0,len(test_number)):
            add_number = add_number + int(test_number[x])
        add_number = add_number + int(test_number)
        if add_number == ognumber:
            junction_list.append(int(test_number))
​
    if len(junction_list) == 0:
        return "Self"
    else:
        for i in range(0, len(junction_list)):
            junction_list2.append(junction_list[index])
            index -=1
        return junction_list2

