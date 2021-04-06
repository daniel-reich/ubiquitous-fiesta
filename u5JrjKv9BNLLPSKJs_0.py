
def num_ways(n, s):
    ways = [1]
    for _ in range(n):
        ways.append(sum(ways[-len(s):]))
    return ways.pop()

