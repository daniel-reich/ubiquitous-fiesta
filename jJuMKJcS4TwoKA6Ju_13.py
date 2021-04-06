
def dial(txt):
    ans = ''
    for cha in range(len(txt)):
        ltr = txt[cha].lower()
        if ltr in ['a', 'b', 'c']:
            ans += '2'
​
        elif ltr in ['d', 'e', 'f']:
            ans += '3'
​
        elif ltr in ['g', 'h', 'i']:
            ans += '4'
​
        elif ltr in ['j', 'k', 'l']:
            ans += '5'
​
        elif ltr in ['m', 'n', 'o']:
            ans += '6'
​
        elif ltr in ['p', 'q', 'r', 's']:
            ans += '7'
​
        elif ltr in ['t', 'u', 'v']:
            ans += '8'
​
        elif ltr in ['w', 'x', 'y', 'z']:
            ans += '9'
​
        else:
            ans += ltr
    return ans

