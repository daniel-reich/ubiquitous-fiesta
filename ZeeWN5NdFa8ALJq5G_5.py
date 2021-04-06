
def nearest_chapter(chapt, page):
    return min([(v, k) for k, v in chapt.items()],
               key=lambda t: (abs(t[0] - page), page - t[0]))[1]

