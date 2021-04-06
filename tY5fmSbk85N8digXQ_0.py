
def ones_infection(arr):
    infected_r = [max(i) for i in arr]
    infected_c = [max(i) for i in zip(*arr)]
​
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            arr[r][c] = max(infected_r[r], infected_c[c])
            
    return arr

