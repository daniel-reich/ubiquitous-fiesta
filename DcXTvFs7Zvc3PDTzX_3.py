
def validate_binary(b):
  count=0
  for i in b:
    if i=='1':
      count+=1
  return count%2==0

