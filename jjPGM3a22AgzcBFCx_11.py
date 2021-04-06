
def decrypt(lst):
    return [chr(64+x) for x in range(1,27) if not x in lst][0]

