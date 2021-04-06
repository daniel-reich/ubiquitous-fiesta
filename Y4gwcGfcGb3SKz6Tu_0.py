
def max_separator(s):
    substrings = [(s.find(i, idx+1) - idx, i) for idx, i in enumerate(s) if s.find(i, idx+1) != -1]
    return sorted([c for size, c in substrings if size == max(substrings)[0]])

