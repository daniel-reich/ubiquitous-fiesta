
def grant_the_hint(txt):
    word_lst = txt.split()
    fin_str = ""
    fin_arr = []
    longest_word = max(word_lst, key=len)
    for i in range(len(longest_word)+1):
        for word in word_lst:
            fin_str += word[:i] + (len(word)-i)*'_' + ' ' if len(word)-i >= 0 else word+' '
        fin_arr.append(fin_str)
        fin_str = ""
​
    return [l.rstrip() for l in fin_arr]

