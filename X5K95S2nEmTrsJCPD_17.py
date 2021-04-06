
def emotify(txt):
    if "smile" in txt:
        return txt.replace("smile",":D")
    elif "grin" in txt:
        return txt.replace("grin",":)")
    elif "sad" in txt:
        return txt.replace("sad",":(")
    else:
        return txt.replace("mad",":P")

