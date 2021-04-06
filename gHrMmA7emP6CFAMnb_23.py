
def is_apocalyptic(number):
  d= {0:"Safe", 1:"Single", 2:"Double", 3:"Triple"}
  return d[str(2 ** number).count("666")]

