
def count_substring(s):
    cnt = 0
    idxa = s.find('A')
    while idxa != -1:
        cnt+= s[idxa+1:].count('X')
        x = s[idxa+1:].find('A')
        if x == -1:
            break
        idxa += x + 1
    return cnt

