
def prevent_distractions(txt):
    unsafe = ["anime", "vine", "meme", "roasts", "Danny DeVito"]
    for x in unsafe:
        if x in txt:
            return "NO!"
    else:
        return "Safe watching!"

