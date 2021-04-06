
def sort_by_letter(lst):
    if len(lst) == 0:
        return []
    myans = []
    for i in range(26):
        for item in lst:
            if chr(i+97) in item:
                myans.append(item)
                break
    return myans

