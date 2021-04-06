
def lcm_of_list(numbers):
  lcm = 1
  while True:
    for i in numbers:
      if lcm % i != 0:
        break
    else:
      return lcm
    lcm += 1

