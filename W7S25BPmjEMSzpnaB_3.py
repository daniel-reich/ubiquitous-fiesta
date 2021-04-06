
def bonacci(N, k):
    n = -1*N
    numbers = []
    for i in range(N):
        if i < (N-1):
            numbers.append(0)
        else:
            numbers.append(1)
    for i in range(k):
        if i == (k-1):
            numbers.append(sum(numbers[n:]))
            return(numbers[i])
        elif i < (N-1):
            continue
        else:
            numbers.append(sum(numbers[n:]))

