
def portion_happy(numbers):
  happy = 0
  hacky = [2] + numbers + [2]
  for i in range(1, len(hacky) - 1):
    if hacky[i] == hacky[i - 1] or hacky[i] == hacky[i + 1]:
      happy += 1
  return round(happy / len(numbers), 1)

