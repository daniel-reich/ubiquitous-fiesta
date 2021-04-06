
def count_substring(s):
    return sum(s[i] == 'A' and s[j] == 'X' for i in range(len(s) - 1) for j in range(i+1, len(s)))

