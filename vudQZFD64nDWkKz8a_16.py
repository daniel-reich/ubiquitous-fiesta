
def grant_the_hint(txt):
    def word_show(word,n):
        return word[:n] + ('_' * (len(word) - n))
    final = []    
    words_list = txt.split()
    max_len = max([len(word) for word in words_list])
    for i in range(0,max_len+1):
        res = ''
        for word in words_list:
            res += word_show(word,i) + ' '
        final.append(res.rstrip())
    return final

