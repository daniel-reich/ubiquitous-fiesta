
def binary_to_decimal(binary):
  binary.reverse()
  sum=0
  for i in range(len(binary)):
    sum=sum+binary[i]*(2**i)
  return sum

