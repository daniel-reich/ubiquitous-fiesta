
def min_turns(current, target):
    lst_current = list(map(int, current)) 
    lst_target = list(map(int, target)) 
    lst_ = []
    for i in range(4):
        if abs(lst_current[i] - lst_target[i]) < 10 - abs(lst_current[i] - lst_target[i]):
            lst_.append(abs(lst_current[i] - lst_target[i]))
        else:
            lst_.append(10 - abs(lst_current[i] - lst_target[i]))
    return sum(lst_)

