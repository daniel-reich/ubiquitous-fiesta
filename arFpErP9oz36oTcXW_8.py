
def secret(txt):
    hclass = ' '.join(txt.split('.')[1:])
    tag = txt.split('.')[0]
    return "<{} class='{}'></{}>".format(tag, hclass , tag)

