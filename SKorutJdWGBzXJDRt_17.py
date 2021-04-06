
msg="Hello {}"
​
​
def greet_people(names):
  gr=''
  message=[]
  for i in names:
      message.append(msg.format(i))
  return(", ".join(message))

