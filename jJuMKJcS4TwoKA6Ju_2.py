
digits = [("abc", "2"), ("def", "3"), ("ghi", "4"), ("jkl", "5"), ("mno", "6"),
          ("pqrs", "7"), ("tuv", "8"), ("wxyz", "9")]
def find_digit(c):
    for s, d in digits:
        if c in s:
            return d
​
def dial(txt):
    return "".join([find_digit(c.lower()) if c.isalpha() else c for c in txt])

