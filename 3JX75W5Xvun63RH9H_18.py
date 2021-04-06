
def describe_num(n):
  num_desc = {
        1: "brilliant",
        2: "exciting",
        3: "fantastic",
        4: "virtuous",
        5: "heart-warming",
        6: "tear-jerking",
        7: "beautiful",
        8: "exhilarating",
        9: "emotional",
        10: "inspiring"
        }
  y = []
  for x in range(1, 11):
    if not n % x:
      y.append(x)
  return "The most {} number is {}!".format(" ".join(num_desc[z] for z in y), n)

