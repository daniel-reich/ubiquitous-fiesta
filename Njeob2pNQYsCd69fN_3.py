
def prevent_distractions(txt):
    keywords = ("Anime", "Animes", "Meme", "Memes", "Vine", "Vines", "Roasts", "Roast", "Danny", "Devito")
    status = 'Safe watching!'
    for word in txt.title().split():
        if word in keywords:
            status = 'NO!'
            break
        else:
            continue
​
    return status

