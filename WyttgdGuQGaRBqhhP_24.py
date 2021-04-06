
def min_palindrome_steps(txt):
    txt_list = list(txt)
    temp = txt_list.copy()
    if txt == txt[::-1]:
        return 0
    for i in range(1, len(txt_list)+1):
        reverse = reversed(txt_list[0:i])
        temp.extend(reverse)
        if temp == temp[::-1]:
            return i
        else:
            temp = txt_list.copy()
            continue

