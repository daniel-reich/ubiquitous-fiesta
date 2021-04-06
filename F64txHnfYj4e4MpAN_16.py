
def schoty(frame):
    return int(''.join([str(len(i[0:i.index('-')])) for i in frame]))

