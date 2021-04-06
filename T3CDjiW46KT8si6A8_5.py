
def product(lst):
    a = [i for i in sorted(set(lst))]
    try: return max(a) * a[-2]
    except: return a[0] * a[0]

