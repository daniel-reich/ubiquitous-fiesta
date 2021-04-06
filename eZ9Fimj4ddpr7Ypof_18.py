
def mumbling(s):
    return '-'.join([(x*i).capitalize()
                     for i, x in enumerate(s, start=1)])

