
def invert(s):
    if not s:
        return s
    if len(s) == 1:
       if s.islower():
           return s.upper()
       elif s.isupper():
           return s.lower()
       else:
           return s
    else:
        if s[-1].islower():
            return s[-1].upper() + invert(s[:-1])
        elif s[-1].isupper():
            return s[-1].lower() + invert(s[:-1])
        else:
            return s[-1] + invert(s[:-1])

