
def nearest_chapter(chapt, page):
  return min(chapt, key = lambda ch: (abs(chapt[ch]-page), -chapt[ch]))

