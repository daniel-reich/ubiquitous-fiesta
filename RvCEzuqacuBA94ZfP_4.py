
def generate_hashtag(txt):
    s = "".join(txt.strip().title().split())
    return "#{}".format(s) if 0 < len(s) < 140 else False

