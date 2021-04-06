
def final_countdown(lst):
    count = sum(map(lambda x : x == 1, lst))
    if lst == []:
       return [0, []] 
    else:
        a = []
        count_down_list = []
        for i in range(len(lst)):
            if lst[i] == 1:
                a.append(i)
        for i in range(len(a)):
            if i == 0:
                j = a[i]
                b = [1]
                yes = True
                while (j > -1) & (yes ==True):
                    if lst[j-1] == lst[j] + 1:
                        b.append(lst[j-1])
                        yes = True
                    else:
                        yes = False
                    j -= 1
                b.reverse()
                count_down_list.append(b)
            elif (i>0) & (a[i]-a[i-1]==1):
                count_down_list.append([1])
            else:
                j = a[i]
                b = [1]
                yes =True
                while (j > a[i-1]) & (yes== True):
                    if lst[j-1] == lst[j] + 1:
                        b.append(lst[j-1])
                        yes = True
                    else:
                        yes = False
                    j -= 1
                b.reverse()
                count_down_list.append(b)
        return [count, count_down_list]

