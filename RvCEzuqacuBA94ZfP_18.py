
def generate_hashtag(txt):
    if set(list(txt)) == {' '}: return False
    res = "#{}".format("".join([i.capitalize() for i in txt.split()])) if txt != "" else False
    try:
        return res if len(res) <= 140 else False
    except:
        return False

