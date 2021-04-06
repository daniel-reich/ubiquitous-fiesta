
def hours_passed(time1, time2):
  hours = ""
  if time1 == time2:
    hours = "no time passed"
​
  elif time1[5:7] == "AM" and time2[5:7] == "AM":
    passTime = int(time2[:time2.index(":")]) - int(time1[:time1.index(":")])
    hours = "{0} hours".format(passTime)
  
  elif time1[5:7] == "PM" and time2[5:7] == "PM":
    passTime = int(time2[:time2.index(":")]) - int(time1[:time1.index(":")])
    hours = "{0} hours".format(passTime)
  
  elif time1[5:7] == "AM" and time2[5:7] == "PM":
    passTime = int(time2[:time2.index(":")]) + 12 - int(time1[:time1.index(":")])
    hours = "{0} hours".format(passTime)
​
  elif time1[5:7] == "PM" and time2[5:7] == "AM":
    passTime = int(time2[:time2.index(":")]) + 12 - (int(time1[:time1.index(":")]))
    hours = "{0} hours".format(passTime)
      
  return hours

