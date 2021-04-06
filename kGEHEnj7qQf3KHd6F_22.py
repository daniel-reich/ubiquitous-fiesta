
import string
def alphanumeric_restriction(s):
  abc = s.isalpha()
  num = s.isnumeric()
  if(abc and not num):
    return(True)
  if(num and not abc):
    return(True)
  if(not num and not abc):
    return(False)

