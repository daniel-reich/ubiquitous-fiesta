
def simple_numbers(a, b):
  return [i for i in range(a,b+1) if sum(int(str(i)[j])**(j+1) for j in range(len(str(i)))) == i or i < 10]

