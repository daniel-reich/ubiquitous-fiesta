
def final_result(lst):
    for i in range(len(lst) - 1):
        match = False
        for j in range(i + 1, len(lst)):
            if lst[i] ==  lst[j]:
                match = True
            else:
                break
        if match == True:
            if j == len(lst) - 1 and lst[j] == lst[j - 1]:
                j += 1
            del lst[i:j]
            return final_result(lst)
    return lst

