
def final_countdown(lst):
    result = [0, []]
    lst = lst[::-1]
    countdown = []
    for i in lst:
        if i == 1:
            if countdown == []:
                countdown.append(i)
            else:
                result[0] += 1
                result[1].append(countdown[::-1])
                countdown = [i]
        elif countdown != []:
            if i-1 == countdown[-1]:
                countdown.append(i)
            else:
                result[0] += 1
                result[1].append(countdown[::-1])
                countdown = []
    if countdown != []:
        result[0] += 1
        result[1].append(countdown[::-1])
    result[1] = result[1][::-1]
    return result

