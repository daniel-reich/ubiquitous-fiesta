
def prime_numbers(num):
  return len([numm for numm in range(2,num+1) if all([0 if numm%c==0 else 1 for c in range(2,numm)])])

