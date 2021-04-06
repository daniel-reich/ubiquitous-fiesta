
def count_substring(s):
    substrings = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == 'A' and s[j] == 'X':
                substrings += 1
    return substrings

