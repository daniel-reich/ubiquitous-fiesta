
def num_args(func):
  for i in range(20):
    try:
        a = [e for e in range(i)]
        func(*a)
        return i
    except:
      continue

