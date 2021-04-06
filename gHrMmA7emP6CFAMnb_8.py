
def is_apocalyptic(number):
  ans = 2 ** number
  count_v = str(ans).count("666")
  if count_v == 0:
    return "Safe"
  elif count_v == 1:
    return "Single"
  elif count_v == 2:
    return "Double"
  elif count_v == 3:
    return "Triple"

