
def even_or_odd(s):
  even = sum(int(i) for i in s if int(i) % 2 ==0);
  odd = sum(int(i) for i in s if int(i) % 2 ==1);
  if even == odd:
    return 'Even and Odd are the same';
  elif odd > even:
    return "Odd is greater than Even";
  return "Even is greater than Odd";

