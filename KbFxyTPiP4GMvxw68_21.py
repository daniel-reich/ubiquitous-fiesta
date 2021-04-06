
def longest_zero(s):
  lst=s.split("1")
  result=["0"*max(len(chain) for chain in lst)]
  return "".join(result)

