
def mystery_func(num):
  prev = 0
  asd = 2
  count = 1
  while True:
    prev = asd
    asd =+ asd * 2
    if asd > num:
      return int((count * '2') + str(num - prev))
    count += 1

