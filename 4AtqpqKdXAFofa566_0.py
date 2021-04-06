
def remove_leading_trailing(n):
    s = str(float(n))
    return s[:-2] if s.endswith('.0') else s

