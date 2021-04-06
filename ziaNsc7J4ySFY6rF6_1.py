
def will_fit(holds, cargo):
    d = {"S":50, "M":100, "L":200}
    holds = sum([d[i] for i in holds])
    return holds >= sum(cargo)

