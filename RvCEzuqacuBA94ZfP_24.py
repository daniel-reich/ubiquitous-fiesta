
def generate_hashtag(txt):
    result = "#" + "".join(txt.title().strip().split())
    if len(result) > 140 or len(result) == 1:
        return False
    else:
        return result

