
def sock_pairs(socks):
    count=0
    count_2=0
    count_3=1
    array=[]
    array_2=[]
    for x in range(len(socks)):
        array.append(socks[x])
    array.sort()
    for z in range(len(array)-1):
        try:
            if(array[z+count_2]==array[z+count_3]):
                array_2.append(array[z+count_2]+array[z+count_3])
                count_2+=1
                count_3+=1
        except IndexError:
            pass
        continue
    return len(array_2)

