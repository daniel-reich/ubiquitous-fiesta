
def organize(s):
    if not s:
        return {}
    d = dict(zip(('name', 'age', 'occupation'), s.split(', ')))
    d['age'] = int(d['age'])
    return d

