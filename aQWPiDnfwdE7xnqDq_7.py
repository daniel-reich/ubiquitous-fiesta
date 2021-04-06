
def drange(*args):
    my_list = []
    dec = []
    final_list = []
    round_dig = 0
    round_num = 0
    for i in range (0,len(args)):
        my_str = str(args[i])
        dec = my_str.split(".")
        if (len(dec) == 2):
            round_dig = len(dec[1])
            final_list.append(round_dig)
    
    if (final_list == []):
        round_num = 0
    elif (len(final_list) == 1):
        round_num = int(final_list[0])
    else:
        final_list.sort()
        final_list.reverse()
        round_num = int(final_list[0])
    
    num = args[0]
    
    if (len(args) == 3):
        my_tup = ()
        my_tup = my_tup + (num,)
        while(num<args[1]):
            num+=args[2]
            num = round(num,round_num)
            my_tup = my_tup + (num,)
        return my_tup[0:len(my_tup)-1]
    elif (len(args) == 2):
        my_tup = ()
        for i in range (args[0],args[1]):
            my_tup = my_tup + (i,)
        return my_tup
    elif (len(args) == 1):
        my_tup = ()
        for i in range (0,args[0]):
            my_tup = my_tup + (i,)
        return my_tup
            
            
            
print(drange(10))

