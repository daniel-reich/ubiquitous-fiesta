
def staircase(n):
  def line(m):
    return "_" * (abs(n) - m) + "#" * m
  def function(i):
    return line(abs(n)+1-i) if n < 0 else line(i)
​
  return ''.join(list(map(lambda x: function(x) + "\n", range(1,abs(n)+1)))).rstrip("\n")

