
def split_n_cases(txt, cases):
    s = len(txt) // cases
    return [txt[s*(i-1):s*i] for i in range(1, cases+1)] if s*cases == len(txt) else ['Error']

