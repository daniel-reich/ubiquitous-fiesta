
def arrow(num):
  result = [">" * i for i in range(1, num + 1)]
  if num % 2 == 0:
    return result + result[::-1]
  return result + result[:-1][::-1]

