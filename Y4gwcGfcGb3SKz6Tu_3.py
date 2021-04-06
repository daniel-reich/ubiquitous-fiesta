
def max_separator(s):
    lst, length = [], 2
    for i in range(len(s)-1):
        for j in range(i,len(s)):
            if s[i] == s[j] and s[i:j+1].count(s[i]) == 2:
                if j-i+1 == length:
                    lst.append(s[i])
                elif j-i+1 > length:
                    length = j-i+1
                    lst = [s[i]]
    return sorted(lst)

