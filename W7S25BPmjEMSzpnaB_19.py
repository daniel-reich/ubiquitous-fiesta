
def bonacci(N, k):
    Numbers = []
    for i in range(k):
        if(i < N -1):
            Numbers.append(0)
        elif(i == N - 1):
            Numbers.append(1)
        else:
            Numbers.append(sum(Numbers[-N:]))
    return Numbers[-1]

