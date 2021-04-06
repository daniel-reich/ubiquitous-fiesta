
def lcm(arr):
  if len(arr)==1: return arr[0]
  gcd = lambda a,b: a if not b else gcd(b, a%b)
  results = arr[0]*arr[1]//gcd(arr[0],arr[1])
  for x in arr[2:]: results = results*x//gcd(results,x)
  return results

