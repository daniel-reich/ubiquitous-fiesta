
def convert_binary(string):
  a = string.lower()
  ans = ""
  for i in range(0 , len(a)):
    if ord(a[i]) >= 97 and ord(a[i]) <= 109:
      ans += "0"
    else:
      ans += "1"
  return ans

