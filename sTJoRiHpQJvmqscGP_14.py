
def daily_streak(lst):
    otvet = []
    p=0
    for i in range(len(lst)):
        if lst[i]==True:
            p+=1
        else:
            p=0
        otvet.append(p)
    return max(otvet)

