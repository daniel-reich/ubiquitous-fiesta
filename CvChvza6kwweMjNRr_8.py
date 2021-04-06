
def split_code(item):
    return [''.join(x for x in item if x.isalpha()),int(''.join(x for x in item if x.isdecimal()))]

