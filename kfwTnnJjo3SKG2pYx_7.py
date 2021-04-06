
def replace_nums(input_string):
    num = ''
    int_list = []
​
    for i in range(0,len(input_string)):
        try:
            if isinstance(int(input_string[i]),int) == True:
               num += input_string[i]
        
        except:
            if num != '':
                int_list.append('{0:b}'.format(int(num)))
     
            int_list.append(input_string[i])
            num = ''
​
    return ''.join(int_list)

