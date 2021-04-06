
def nearest_chapter(chapt, page):
  return min(chapt.items(), key=lambda kv: (abs(kv[1]-page), -kv[1]))[0]

