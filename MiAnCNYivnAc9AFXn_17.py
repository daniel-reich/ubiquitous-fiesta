
def change_types(lista):
    strings = lambda x: x.capitalize() + '!' if isinstance(x, str) else \
        not x if isinstance(x, bool) else (x + 1) if isinstance(x, int) and x % 2 == 0 else x
    return list(map(strings, lista))

