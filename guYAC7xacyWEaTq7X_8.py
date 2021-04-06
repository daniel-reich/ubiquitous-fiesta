
def is_autobiographical(n):
  auto = tuple(map(int, str(n)))
  return all(
    auto.count(index) == number 
    for index, number in enumerate(auto)
  )

