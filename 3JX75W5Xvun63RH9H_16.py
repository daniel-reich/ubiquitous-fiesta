
def describe_num(n):
  adjetivos = []
  if n%1==0:
    adjetivos.append("brilliant")
  if n%2==0:
    adjetivos.append("exciting")
  if n%3==0:
    adjetivos.append("fantastic")
  if n%4==0:
    adjetivos.append("virtuous")
  if n%5==0:
    adjetivos.append("heart-warming")
  if n%6==0:
    adjetivos.append("tear-jerking")
  if n%7==0:
    adjetivos.append("beautiful")
  if n%8==0:
    adjetivos.append("exhilarating")
  if n%9==0:
    adjetivos.append("emotional")
  if n%10==0:
    adjetivos.append("inspiring")
  return("The most " + (' '.join(adjetivos)) + " number is " + str(n) + "!")

