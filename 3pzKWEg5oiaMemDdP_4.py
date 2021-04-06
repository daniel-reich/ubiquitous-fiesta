
def most_expensive_item(products):
  top=0
  ans=''
  for i in products:
    if products[i]>top:
      top=products[i]
      ans=i
  return ans

