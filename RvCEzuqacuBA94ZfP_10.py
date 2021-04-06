
def generate_hashtag(txt):
    txt = "".join([i.title() for i in txt.split(" ")])
    return False if len(txt) == 0 or len(txt) >= 140 else "#" + txt

