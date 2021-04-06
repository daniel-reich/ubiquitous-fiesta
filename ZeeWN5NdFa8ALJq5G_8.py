
def nearest_chapter(chapt, page):
  return sorted(chapt.items(), key=lambda d: (abs(d[1] - page), -d[1]))[0][0]

