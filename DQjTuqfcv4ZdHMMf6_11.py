
def kaprekar(num):
  iterations = 0
  outcome = str(num)
  while int(outcome) != 6174:
    iterations += 1
    largest = int(''.join(sorted(str(outcome), reverse=True)))
    smallest = int(''.join(sorted(str(outcome))))
    if str(smallest)[0] == 0:
      smallest = int(str(smallest)[1:])
    outcome = largest - smallest
    if int(outcome) < 1000:
      outcome = '0' + str(outcome)
  return iterations

