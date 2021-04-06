
def staircase(n, hashs = 1):
    if abs(n) == hashs: return abs(n) * "#"
    return staircase(n, hashs + 1) + "\n" + (abs(n) - hashs) * "_" + hashs * "#"  if n < 0 else  (n - hashs) * "_" + hashs * "#" +"\n" +  staircase(n, hashs + 1)

