
def nearest_chapter(chapt, page):
  chapt = {v:k for k, v in chapt.items()}
  return chapt[min(sorted(chapt, reverse=True), key=lambda x: abs(x-page))]

