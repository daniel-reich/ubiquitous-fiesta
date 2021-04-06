
def nearest_chapter(chapt, page):
    return sorted(chapt.items(), key=lambda x: (abs(x[1] - page), -x[1]))[0][0]

