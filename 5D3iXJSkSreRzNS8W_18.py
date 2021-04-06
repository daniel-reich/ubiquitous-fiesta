
def news_at_ten(txt, n):
    txt = n * ' ' + txt + 2 * n * ' ' 
    ans = [txt[i:i + n] for i in range(len(txt) + 1 - (2 * n))]
    return ans

