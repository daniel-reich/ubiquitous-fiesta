
def is_palindrome(txt):
    rev_txt_list = list(txt)
    rev_txt_list.reverse()
    rev_txt = "".join(rev_txt_list)
    if (rev_txt == txt):
        return 1
    else:
        return 0
​
​
def min_palindrome_steps(txt):
    if (is_palindrome(txt)):
        return 0
    else:
        for num_add in range(len(txt)):
            new_string = txt + txt[num_add:0:-1] + txt[0]
            if (is_palindrome(new_string)):
                return num_add + 1

