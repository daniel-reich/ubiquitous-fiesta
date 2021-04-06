
def count_layers(rug):
    count = 1
    val1 = len(rug)
    q1 = val1//2
    val2 = len(rug[q1])
    q2 = val2//2
    for i in range(q2):
        if rug[q1][i] != rug[q1][i+1]:
            count = count + 1
    return(count)

