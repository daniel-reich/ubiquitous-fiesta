
def validate(s):
    if s[0] == "+":
        s = s[1:]
    s = s[::-1]
    s = numeric(s, 4)
    for _ in range(2):
        s = delimiter(s)
        s = numeric(s, 3)
​
    if s == "" or s == "(":
        return True
    s = delimiter(s)
    if s == "1":
        return True
    return False
    
def numeric(s, x):
    for i in range(x):
        if not s[i].isnumeric() or len(s) < x:
            s = "FALSE"
    s = s[x :]
    return s
    
def delimiter(s):
    if s[: 2] in ["( ", " )"]:
        s = s[2 :]    
    elif s[0] in [" ", "-", ".", "/"]:
        s = s[1 :]
    return s

