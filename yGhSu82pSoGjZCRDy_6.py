
def seesaw(int_1):
    if(int_1==None):
        return "balanced"
    string=str(int_1)
    array=[]
    array_2=[]
    array_3=[]
    int_2=0
    int_3=0
    for x in range(len(string)):
        array.append(string[x])
    if(len(array)==1):
        return "balanced"
    if(len(array)%2!=0):
        array.remove(array[int(len(array)/2)])
        for z in range(int(len(array)/2)):
            array_2.append(array[z])
            array.remove(array[z])
        int_3=int("".join(array))
        int_2=int("".join(array_2))
        if(int_2>int_3):
            return 'left'
        if(int_2<int_3):
            return 'right'
        if(int_2==int_3):
            return 'balanced'
    elif(int_1!=None):
        for z in range(int(len(array)/2)):
            array_2.append(array[z])
        for i in range(len(array_2)):
            array.remove(array_2[i])
        int_3=int("".join(array))
        int_2=int("".join(array_2))
        if(int_2>int_3):
            return 'left'
        if(int_2<int_3):
            return 'right'
        if(int_2==int_3):
            return 'balanced'

