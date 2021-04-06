
def collatz(num):
  return 0 if num==1 else 1 + collatz(num/2) if not num%2 else 1+collatz(num*3+1)

