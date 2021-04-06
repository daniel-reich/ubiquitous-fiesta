
def blah_blah(txt, n):
    txt = txt.split()
    if n > len(txt):
        return (" blah" * len(txt)).lstrip() + "..."
    words = " ".join(txt[:-n])
    return words + (" blah" * n) + "..."

