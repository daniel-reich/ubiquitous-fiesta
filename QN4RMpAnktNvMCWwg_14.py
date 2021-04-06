
def id_mtrx(n):
    my_zero_mtrx = []
    if (type(n) == str):
        return "Error"
    my_list = [0]*n
    my_zero_list = []
    my_idt_mtrx = []
    
    if (n==0):
        my_idt_mtrx = [[]]
        return my_idt_mtrx
    
    elif (n>0):
        j=0
        for i in range (0,n):
            my_zero_mtrx.append(my_list)
        for i in range (0,len(my_zero_mtrx)):
            my_zero_list = my_zero_mtrx[i]
            my_zero_list = [0]*n
            my_zero_list[j] = 1
            my_idt_mtrx.append(my_zero_list)
            j+=1
        return my_idt_mtrx
    elif (n<0):
        j = len(my_list)-1
        for i in range (0,abs(n)):
            my_zero_mtrx.append(my_list)
        for i in range (0,len(my_zero_mtrx)):
            my_zero_list = my_zero_mtrx[i]
            my_zero_list = [0]*abs(n)
            my_zero_list[j] = 1
            my_idt_mtrx.append(my_zero_list)
            j-=1
        return my_idt_mtrx
        
        
 
​
print(id_mtrx("4"))

