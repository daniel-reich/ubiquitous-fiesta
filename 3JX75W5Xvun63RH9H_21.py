
def describe_num(n):
  l = ""
  
  if n%1==0:
    l+="brilliant"
    l+=" "
  if n%2==0:
    l+="exciting"
    l+=" "
  if n%3==0:
    l+="fantastic"
    l+=" "
  if n%4==0:
    l+="virtuous"
    l+=" "
  if n%5==0:
    l+="heart-warming"
    l+=" "
  if n%6==0:
    l+="tear-jerking"
    l+=" "
  if n%7==0:
    l+="beautiful"
    l+=" "
  if n%8==0:
    l+="exhilarating"
    l+=" "
  if n%9==0:
    l+="emotional"
    l+=" "
  if n%10==0:
    l+="inspiring"
    l+=" "
  txt="number is {}"
  x = txt.format(n)
  return "The most"+" "+''.join(l)+x+"!"

