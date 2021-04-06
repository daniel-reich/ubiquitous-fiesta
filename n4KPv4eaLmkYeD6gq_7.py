
def face_interval(num):
  if type(num)!= list:
    return ":/"
  r = num[-1]-num[0]
  return (":)" if r in num else ":(" )

