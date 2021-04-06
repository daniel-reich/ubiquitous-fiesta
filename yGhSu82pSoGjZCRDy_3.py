
def seesaw(num):
  def helper(pastmiddle):
    if int(str(num)[:middle]) > int(str(num)[pastmiddle:]):
      return "left"
    elif int(str(num)[:middle]) < int(str(num)[pastmiddle:]):
      return 'right'
    else:
      return 'balanced'
  middle = int(len(str(num))/2)
  if not num or len(str(num)) == 1:
    return 'balanced'
  elif len(str(num)) %  2 == 0:
    return helper(middle)
  else:
    return helper(middle+1)

