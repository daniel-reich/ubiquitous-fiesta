
def nearest_chapter(chapt, page):
  return sorted(((c, p, abs(p-page)) for c, p in chapt.items()), key=lambda x: (x[-1], -x[-2]))[0][0]

