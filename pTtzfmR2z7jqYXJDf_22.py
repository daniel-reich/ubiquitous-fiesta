
def possible_palindrome(txt):
    txt_lst = list(txt)
    txt_set = list(set(txt))
    count_odd = 0
    
    for i in txt_set:
        if txt_lst.count(i) % 2 != 0:
            count_odd += 1
    if count_odd > 1:
        return False
    else:
        return True

