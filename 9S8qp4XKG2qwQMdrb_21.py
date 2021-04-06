
def ways_to_climb(n):
    if n<=1:
        return 1
    if n<=2:
        return 2
    return ways_to_climb(n-1)+ways_to_climb(n-2)

