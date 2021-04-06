
def boom_intensity(n):
  if n < 2:
    return "boom"
  result = "B{}m{}".format("o"*n, "!" if not n%2 else "")
  return result.upper() if not n%5 else result

