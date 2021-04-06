
def organize(txt):
    if len(txt) == 0:
        return {}
    name, age, occ = txt.split(',')
    return {'name': name.strip(), 'age': int(age), 'occupation': occ.strip()}

