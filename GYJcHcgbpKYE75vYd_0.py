
def return_end_of_number(num):
  if 11 <= num % 100 <= 13 or not (1 <= num % 10 <= 3):
    return "%d-TH" % num
  return "%d-%s" % (num, ["ST", "ND", "RD"][num % 10 - 1])

