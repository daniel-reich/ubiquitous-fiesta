
def digital_vowel_ban(n, ban):
  
  numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
  '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
  
  answer = ''
  for num in str(n):
    if ban not in (numbers[num]):
      answer += num
  
  if not answer:
    return 'Banned Number'
    
  return int(answer)

