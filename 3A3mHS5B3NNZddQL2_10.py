
def interview(lst, tot):
​
  Categories = [  "very easy", "very easy", "easy", "easy", 
                  "medium", "medium", "hard", "hard"  ]
  
  Total_Time = 0
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    
    Standard = Categories[Counter]
    Time_Spent = lst[Counter]
    
    if (Standard == "very easy") and (Time_Spent <= 5):
      Total_Time += Time_Spent
      Counter += 1
    elif (Standard == "easy") and (Time_Spent <= 10):
      Total_Time += Time_Spent
      Counter += 1
    elif (Standard == "medium") and (Time_Spent <= 15):
      Total_Time += Time_Spent
      Counter += 1
    elif (Standard == "hard") and (Time_Spent <= 20):
      Total_Time += Time_Spent
      Counter += 1
    else:
      return "disqualified"
      
  if (len(lst) == 8) and (tot <= 120):
    return "qualified"
  else:
    return "disqualified"

