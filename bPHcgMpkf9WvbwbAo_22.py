
def format_phone_number(lst):
  answer = "("
  for i in range(3):
    answer += str(lst[i])
  answer += ") "
  for i in range(3):
    answer += str(lst[i+3])
  answer += "-"
  for i in range(4):
    answer += str(lst[i+6])
  return answer

