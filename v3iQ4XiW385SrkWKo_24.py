
def final_result(lst):
    if len(lst) <= 1:
        return lst
    elif len([i for i in range(1,len(lst)) if lst[i] != lst[i-1]]) == len(lst)-1:
        return lst
    else:
        unmentionables = []
        lst_len = len(lst)
        start = 0
        while start < lst_len:
            start += 1
            if lst[start] == lst[start-1]:
                unmentionables.append(start-1)
                elem = lst[start]
                check = start
                while check < lst_len and lst[check] == elem:
                    unmentionables.append(check)
                    check += 1
                for i in unmentionables[::-1]:
                    del lst[i]
                return final_result(lst)

