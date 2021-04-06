
def sorting(s):
    new_key = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789'
    return ''.join(sorted(s, key=new_key.index))

