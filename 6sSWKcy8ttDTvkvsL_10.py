
def afterNdays(days, n):
  days2int = { "Sunday" : 0, 
               "Monday" : 1,
               "Tuesday" : 2,
               "Wednesday" : 3,
               "Thursday" : 4,
               "Friday" : 5,
               "Saturday" : 6 }
  int2days = { 0 : "Sunday",
               1 : "Monday",
               2 : "Tuesday",
               3 : "Wednesday",
               4 : "Thursday",
               5 : "Friday",
               6 : "Saturday" }
  return [ int2days[(days2int[day] + n) % 7] for day in days ]

