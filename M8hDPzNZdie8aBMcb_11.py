
def count_substring(txt: str) -> int:
    return sum(txt[i:].count('X') for i,v in enumerate(txt[:-1]) if v == 'A')

