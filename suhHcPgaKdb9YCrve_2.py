
def even_or_odd(s):
  even_sum = sum([int(x) for x in s if int(x)%2 == 0])
  odd_sum = sum([int(x) for x in s if int(x)%2 == 1])
  return "Odd is greater than Even" if odd_sum>even_sum else "Even is greater than Odd" if odd_sum<even_sum else "Even and Odd are the same"

