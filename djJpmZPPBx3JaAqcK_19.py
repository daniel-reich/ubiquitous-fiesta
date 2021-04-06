
def maya_number(n):
  digits = ["@", "o", "oo", "ooo", "oooo", "-", "o-", "oo-", "ooo-", "o o o o -",
          "--","o--", "oo--", "ooo--", "oooo--", 
          "---", "o---", "oo---", "ooo---","oooo---"]
  ret = []
  if n == 0: return ["@"]
  while n > 0:
    ret.append(digits[n % 20])
    n = n // 20
  return ret[::-1]

