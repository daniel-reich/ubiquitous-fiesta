
def bell_triangle_row(n):
    if n <= 1: return [1]
    previous = bell_triangle_row(n-1) 
    result, i = [previous[-1]], 1
    while len(result) <= len(previous):
        result.append(result[i-1] + previous[i-1])
        i += 1
    return result
​
def bell(n):
    return bell_triangle_row(n)[-1]

