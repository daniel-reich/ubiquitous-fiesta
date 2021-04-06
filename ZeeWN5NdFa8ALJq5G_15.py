
def nearest_chapter(chapt, page):
    c = list(chapt.items())
    return sorted(c,key=lambda x: (abs(page-x[1]),-x[1]))[0][0]

