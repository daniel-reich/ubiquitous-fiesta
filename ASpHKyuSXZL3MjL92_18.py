
def amplify(num):
    integers=[]
    amp_integers= []
    for int in range(1, num+1):
        integers.append(int)
    for item in integers:
        if item%4!=0:
            amp_integers.append(item)
        elif item%4==0:
            amp_integers.append(item*10)
            
    return(amp_integers)

