
def lcm_of_list(numbers):
    lcm_1 = 1
    for i in range(len(numbers)):
        lcm_num = findlcm(lcm_1, numbers[i])
        lcm_1 = lcm_num
    return(lcm_1)
    
    
def findlcm(a, b):   # Function definition
    if(a > b):   
        maximum = a
    else:
        maximum = b
    while(True):
        if(maximum % a == 0 and maximum % b == 0):
            lcm = maximum;
            break;
        maximum = maximum + 1
    return lcm

