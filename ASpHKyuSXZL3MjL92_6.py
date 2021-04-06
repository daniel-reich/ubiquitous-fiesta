
def amplify(num):
  lst = [i if i % 4 else i * 10 for i in range(1, num+1)]
  return lst

