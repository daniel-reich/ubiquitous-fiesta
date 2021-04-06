
def round_number(num, n):
    i=num
    my_list = []
    while(i%n!=0):
        i+=1
    my_list.append(i)
    
    j=num
    while(j%n!=0):
        j-=1
    my_list.append(j)
    #print(my_list)
    diff_list = []
    diff_list.append(abs(my_list[0]-num))
    diff_list.append(abs(my_list[1]-num))
    #print(diff_list)
    if (diff_list[0] == diff_list[1]):
        return my_list[0]
    elif(diff_list[0]<diff_list[1]):
        return my_list[0]
    else:
        return my_list[1]
        
​
​
print(round_number(33, 25))

