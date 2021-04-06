
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
def strong_password(p):
  criteria = [0,0,0,0]
  for i in p:
    if i in numbers: criteria[0] = 1
    if i in lower_case: criteria[1] = 1
    if i in upper_case: criteria[2] = 1
    if i in special_characters: criteria[3] = 1
  if all(criteria) and len(p) > 5: return 0
  if len(p) > 5: return 4-sum(criteria)
  return max(6-len(p), 4-sum(criteria))

