
def prevent_distractions(txt):
  words = ["anime",
          "meme",
          "vine",
          "roasts",
          "Danny DeVito"
          ]
  if any(x in txt for x in words):
    return 'NO!'
  else:
    return 'Safe watching!'

