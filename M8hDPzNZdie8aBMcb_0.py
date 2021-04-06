
def count_substring(s):
    cnt = 0
    for i in range(len(s) - 1):
        if s[i] == 'A':
            cnt += s[i+1:].count('X')
    return cnt

