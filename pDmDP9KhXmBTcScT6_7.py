
import re
​
def get_name(userName): 
​
  userName = userName.split("@")
  userFilter = filter(str.isalpha, userName[0])
  userName[0] = ''.join(userFilter)
​
  return userName[0]

