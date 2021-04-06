
def simple_numbers(a, b):
  return [num for num in range(a, b+1) if num == sum(int(x)**(i+1) for i, x in enumerate(str(num)))]

