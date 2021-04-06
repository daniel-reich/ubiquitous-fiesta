
def remove_leading_trailing(n):
    if '.' in n:
        n = float(n)
    else:
        n = int(n)
    if str(n).endswith('.0'):
        n = str(n).replace('.0', '')
    return str(n)

