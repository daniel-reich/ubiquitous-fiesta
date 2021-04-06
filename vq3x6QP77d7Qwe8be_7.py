
def odd_square_patch(lst): 
    mss = -float('inf')
    for i, x in enumerate(lst):
        indexes, start, count = [], 0, 0
​
        for ind, num in enumerate(x):
            if not num % 2:
                start = ind + 1
                count = 0 
            else:
                count += 1
                indexes.extend([(a, b) for a, b in enumerate(range(count, 0, -1), start) if i + b - 1 < len(lst)])
​
        for a, b in indexes:
            if all(all(item % 2 for item in lst[i+r][a:a+b]) for r in range(b)):
                mss = max(mss, b)
                        
    return max(mss, 0)

