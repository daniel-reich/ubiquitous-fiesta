
def first_place(road):
    lst = []
​
    for item in road:
        if item != "=":
            lst.append(item)
​
    if road == "":
        return None
​
    if lst == []:
        return None
​
    return lst[-1]

