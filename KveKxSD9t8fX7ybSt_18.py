
def final_countdown(lst):
    locd = []
    for i in range(len(lst)):
        if lst[i] == 1:
            cd = [1]
            x = 1
            for j in range(i-1, -1, -1):
                if lst[j] ==  x + 1:
                    cd = [x+1] + cd
                    x += 1
                else:
                    break
            locd.append(cd)
    return [len(locd), locd]

