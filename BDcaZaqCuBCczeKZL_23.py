
def arrow(num):
    w=">"
    output = [">"]
    input=[">"*num]
    if num%2==0:
        for i in range(2,num+1):
            output+=[i*w]
        for i in range(num-1,0,-1):
            input+=[i*w]
    else:
        for i in range(2, num):
            output += [i * w]
        for i in range(num - 1, 0, -1):
            input += [i * w]
​
    return output+input

