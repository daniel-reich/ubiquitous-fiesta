
def paul_cipher(txt):
    txt = txt.upper()
    ans = ''
    for j in txt:
        if j.isalpha():
            ans += j
            prev = j
            break
        else:
            ans += j 
    for i in txt[txt.index(prev) + 1:]:
        if i.isalpha():
            ans += chr((ord(i) + ord(prev) - 129) % 26 + 65)
            prev = i
        else:
            ans += i
    return ans

