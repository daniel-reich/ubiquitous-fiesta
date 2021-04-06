
def manage_delays(train, dest, delay):
  if dest in train.destinations:
​
    time = train.expected_time
​
    x = time.split(":")
    y = [int(i) for i in x]
    print(y)
​
    if delay == 60: 
      y[0] = y[0] + 1 
    elif delay > 60: 
      y[0] = y[0] + delay // 60
      if delay % 60 == 0: 
        pass 
      else:
        if (y[1] + delay % 60) // 60 == 1:
          y[0] = y[0] + 1
          y[1] = (y[1] + delay % 60) % 60  
        else:
          y[1] = y[1] + delay % 60 
    elif delay < 60:
      y[1] = y[1] + delay 
​
    z = ""
    z += str(y[0])
    z += ":"
    if len(str(y[1])) == 2:
      pass
    else:  
      z += str(0)
    z += str(y[1])
    train.expected_time = z

