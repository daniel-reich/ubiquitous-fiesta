
def ways_to_climb(n):
​
    if n <= 1 : return 1
    if n == 2 : return 2
​
    res = [0] * (n+ 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2
​
    for i in range(3 , n + 1):
        res[i] = res[i - 1] + res[i-2]
​
    return res[n]

