
def reorder_digits(lst, direction):
    if direction.startswith('a'):
        return [int(''.join(sorted(str(i)))) for i in lst]
    else:
        return [int(''.join(sorted(str(i), reverse=True))) for i in lst]

