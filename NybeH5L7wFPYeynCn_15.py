
three_letter_collection = lambda s: \
  list() if len(s)<3 else sorted([s[i:i+3] for i in range(len(s)-2)])

