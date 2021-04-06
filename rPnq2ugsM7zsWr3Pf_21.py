
def find_all_digits(lst):
    m = ''
    for i,a in enumerate(lst):
        for b in str(a):
            m+=b
            if ''.join(sorted(set(m)))=='0123456789':
                return a
    return "Missing digits!"

