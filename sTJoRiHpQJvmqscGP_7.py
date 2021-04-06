
def daily_streak(l):
        temp = 0
        m = 0
        for i in range(len(l)):
            print(l[i])
            if l[i]:
                temp += 1
            else:
                if m < temp:
                    m = temp
                temp = 0
        if temp > m:
            m = temp
        return(m)

