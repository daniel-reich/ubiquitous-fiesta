
def flick_switch(lst):
    result = []
    next = True
    for item in lst:
        if type(item) == str and item == 'flick':
            next = not next
        result.append(next)
    return result

