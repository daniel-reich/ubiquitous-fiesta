
def will_fit(holds, cargo):
    space ={'S':50,'M':100,'L':200}
    holds = list(map(lambda x:space[x], holds))
    return sum(cargo)<=sum(holds)

