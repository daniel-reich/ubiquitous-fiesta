
def mapping(letters):
  upper = [x.title() for x in letters]
  return {letters[i]: upper[i] for i in range(len(upper))}

