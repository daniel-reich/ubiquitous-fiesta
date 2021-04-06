
def digit_distance(num1, num2):
    l=[]
    int_1=[int(i) for i in str(num1)]
    int_2=[int(i) for i in str(num2)]
    for i in range(0,len(int_1)):
        l.append(int_2[i]-int_1[i])
    return sum(l)

