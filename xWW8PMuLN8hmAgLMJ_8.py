
def postfix(expression):
    my_list = expression.split(" ")
    new_list=[]
    i=-1
    while len(my_list)>1:
        i+=1
        if str(my_list[i]).replace("-","").isnumeric():
            continue
        else:
            for j in range(i-2):
                new_list.append( my_list[j])
            new_list.append(round(eval(str(my_list[i-2]) + str(my_list[i]) + str(my_list[i-1]))))    
            for j in range(i+1,len(my_list)):   
                new_list.append(my_list[j])        
            my_list=new_list
            new_list=[]
            i=-1
    return int(my_list[0])

