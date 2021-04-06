
def amplify(num):
  return [i if i % 4 != 0 else i * 10 for i in range(1, num+1)]

