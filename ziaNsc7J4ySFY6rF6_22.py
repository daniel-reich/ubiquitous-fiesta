
def will_fit(holds, cargo):
    size = {'S' : 50, 'M' : 100, 'L' : 200}
    return sum([size[x] for x in holds]) >= sum(cargo)

