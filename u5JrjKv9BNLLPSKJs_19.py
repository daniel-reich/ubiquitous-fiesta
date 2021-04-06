
def num_ways(n, s):
    '''
    Returns the number of ways to climb n stairs with each of the number of
    stairs in set s: assumed to go from 1 to a maximum value e.g {1,2,3}.
    '''
    m = max(s)
    temp = 0
    result = [1]
​
    for i in range(1, n + 1):
        j = i - m - 1
        k = i - 1
        if j >= 0:  # i.e possible for this value of i
            temp -= result[j]  # remove elements of previous window
        temp += result[k]
        result.append(temp)
​
    return result[n]

