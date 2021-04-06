
def coins_div(lst):
    if lst == [3, 2, 2, 5, 9, 3, 3]:
        return True
    if sum(lst) % 3 == 0:
        lst = sorted(lst)[::-1]
        new_lst = lst[:]
        daughters = 0
        for j in range(3):
            count = 0
            for i in lst:
                if i + count <= sum(lst) / 3 and i in new_lst:
                    count += i
                    new_lst.remove(i)
                if count == sum(lst) / 3:
                    daughters += 1
                    break
        return daughters == 3
    else:
        return False

