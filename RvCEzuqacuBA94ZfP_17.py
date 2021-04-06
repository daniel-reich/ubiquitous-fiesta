
def generate_hashtag(txt):
    if not txt.isspace() and len(txt) >= 1:
        s = '#' + ''.join(map(str.capitalize, txt.split()))
        return s if 1 <= len(s) <= 140 else False
    return False

