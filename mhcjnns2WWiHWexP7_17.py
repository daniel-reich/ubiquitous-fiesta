
def calculate_arrowhead(lst):
    forward = 0
    backward = 0
    for x in range(0, len(lst)):
        forward = forward + lst[x].count(">")
        backward = backward + lst[x].count("<")
    if forward - backward > 0:
        return(">" * (forward - backward))
    elif forward - backward < 0:
        return("<" * (backward - forward))
    else:
        return("")

