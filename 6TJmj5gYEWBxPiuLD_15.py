
def seating_students(lst):
  K = lst[0]
  seats = [0]*K
  for i in range(1, len(lst)):
    seats[lst[i]-1] = 1
  return sum(1 for i in range(0,K-1,2) if not (seats[i] or seats[i+1])) \
    + sum(1 for i in range(0,K-2) if not (seats[i] or seats[i+2]))

