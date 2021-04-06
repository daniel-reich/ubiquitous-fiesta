
def describe_num(n):
  words = ("brilliant","exciting","fantastic","virtuous","heart-warming",
  "tear-jerking","beautiful","exhilarating","emotional","inspiring")
  
  lst = " ".join(i for x, i in enumerate(words, 1) if n%x==0)
  return "The most {} number is {}!".format(lst, n)

