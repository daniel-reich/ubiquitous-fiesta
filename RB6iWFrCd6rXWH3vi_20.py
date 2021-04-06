
def longest_substring(input):
    sublst=[]
    outputlst=[]
    output=[]
    result=''
    input=list(input)
    length=0
​
​
    for n in range(1, len(input)):
        if n==len(input)-1:
            if int(input[n-1])%2 != int(input[n])%2:
                sublst.append(input[n-1])
                sublst.append(input[n])
                outputlst.append(sublst)
                break
        if int(input[n])%2 != int(input[n-1])%2:
            sublst.append(input[n-1])
        else:
            sublst.append(input[n-1])
            if len(sublst)>1: outputlst.append(sublst)
            sublst=[]
​
​
    for item in outputlst:
        length=max(length,len(item))
​
​
    for item in outputlst:
        if len(item)==length:
            output=item
            break
​
​
    for item in output:
        result=result+str(item)
    print(result)
​
    return(result)

