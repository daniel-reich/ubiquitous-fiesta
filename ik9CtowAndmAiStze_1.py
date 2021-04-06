
def frequency_sort(s):
    return ''.join(sorted(s, key=lambda x: (-s.count(x), -x.isupper(), x.lower())))

