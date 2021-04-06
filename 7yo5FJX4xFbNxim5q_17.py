
def harry(po):
    newlist = []
    total = 0
    if len(po[0]) == 0:
        return -1
    if len(po[0]) == 1:
        return sum(po[0])
    else:
        ### get right down right down
        end_point = (len(po)-1,len(po[0])-1)
        #first combo all the way right then all the way down
        first_right = sum(po[0])
        total += first_right
        for i in range(1,len(po)):
            total += po[i][-1]
        newlist.append(total)
        total = 0
        last_row = po[len(po)-1][1:]
        for i in range(len(po)):
            total += po[i][0]
        total += sum(last_row)
        newlist.append(total)
        return max(newlist)

