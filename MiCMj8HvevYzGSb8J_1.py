
def fibo_word(n):                     # Fibonacci word
  """ Fibonacci sequence but with words """
  arr = ["b", "a"]
  while len(arr) < n: arr.append(arr[-1] + arr[-2])
  return ", ".join(arr) if n>1 else "invalid"

