
def steps_to_convert(txt):
    return min( len([i for i in txt if i.islower()]), len([i for i in txt if i.isupper()]))

