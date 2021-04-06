
def spider_vs_fly(spider, fly):
  label = "ABCDEFGH"
  d = 4 - abs(4 - abs(label.index(spider[0]) - label.index(fly[0])))
  path = [spider]
​
  if abs(int(spider[1]) - int(fly[1]) > 0):
    while spider[1] != fly[1]:
      spider = spider[0] + str(int(spider[1]) - 1)
      path.append("A0" if spider[1] == "0" else spider)
​
  if d > 2:
    while spider[1] != "0":
      spider = spider[0] + str(int(spider[1]) - 1)
      path.append("A0" if spider[1] == "0" else spider)
​
    while spider != fly:
      spider = fly[0] + str(int(spider[1]) + 1)
      path.append(spider)
  else:
    a = label.index(spider[0])
    clockwise = label[(a + d) % 8] == fly[0]
​
    while spider != fly:
      a = (a + (1 if clockwise else -1)) % 8
      spider = label[a] + spider[1]
      path.append(spider)
​
  return "-".join(path)

