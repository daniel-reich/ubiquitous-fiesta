
def nearest_chapter(chapt, page):
  return min(chapt.keys(), key=lambda i: abs(chapt[i]-page-0.5))

