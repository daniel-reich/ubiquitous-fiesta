
def secret_password(message):
  fail_message = 'BANG! BANG! BANG!'
  if len(message) != 9:
    return fail_message
  
  letters = []
  for i in range(0, 3):
    letters.append([]) 
    for j in range(i * 3, i * 3 + 3):
      letter = message[j]
      if 96 < ord(letter) < 123:
        letters[i].append(letter)
      else:
        return fail_message
  
  increment_letter = lambda letter: chr((ord(letter) - 95) % 26 + 96)
  a, b, c = letters
  a[0] = str(ord(a[0]) - 96)
  a[-1] = str(ord(a[-1]) - 96)
  b[0], b[-1] = b[-1], b[0]
  for i in range(3): c[i] = increment_letter(c[i])
  join_parts = lambda *parts: ''.join(''.join(part) for part in parts)
  return join_parts(b, c, a)

