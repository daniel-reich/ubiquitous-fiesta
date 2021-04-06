
def generate_hashtag(txt):
    if len(txt.strip()) == 0:
        return False
    tag = "#"
    for word in txt.split():
        tag += word[0].upper() + word[1:].lower()
    return tag if len(tag) <= 140 else False

