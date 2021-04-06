
def count_layers(rug):
    center=rug[int((len(rug)-1)/2)]
    count=1
    for i in range(1, int((len(center)+1)/2)):
        if center[i]!=center[i-1]:
            count+=1
    return count

