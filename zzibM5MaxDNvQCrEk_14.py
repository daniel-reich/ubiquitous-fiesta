
def will_fit(holds, cargo):
    lst = []
    for i in holds:
        if i == "S":
            lst.append(50)
        elif i == "M":
            lst.append(100)
        elif i == "L":
            lst.append(200)
    return (sum(lst) >=sum(cargo))

