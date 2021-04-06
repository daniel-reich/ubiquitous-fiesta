
def count_substring(s):
    return sum(s[:ind].count('A') for ind,i in enumerate(s) if i=='X')

