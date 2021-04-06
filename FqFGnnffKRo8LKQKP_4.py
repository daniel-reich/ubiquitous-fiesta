
def simple_numbers(a, b):
  l = []
  for x in range(a,b+1):
    print(sum(int(str(x)[i])**i for i in range(len(str(x)))))
    if sum(int(str(x)[i])**(i + 1) for i in range(len(str(x)))) == x:
      l.append(x)
  return l

