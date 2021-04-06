
months = ["NAN", 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
​
def day_of_year(date):
  return (
  int(date.split("/")[1]) +
  
  months[int(date.split("/")[0])] +
  
  (int(date.split("/")[2])%4==0 
  and (int(date.split("/")[2])%100!=0 or int(date.split("/")[2])%400==0)
  and int(date.split("/")[0])>2
  and 1)
  )

