
def seating_students(lst):
  cnt, *used = lst
  return sum(1 for i in range(0,cnt,2) if i+1 not in used and i+2 not in used) + \
        sum(1 for i in range(cnt-2) if i+1 not in used and i+3 not in used)

