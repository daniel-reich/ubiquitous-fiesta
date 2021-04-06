
def camel_to_snake(s):
  ans=''
  for i in s:
    if i.isupper():
      ans+='_'
    ans+=i.lower()
  return ans

