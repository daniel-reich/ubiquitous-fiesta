
def bemirp(n):
  flippable = {'8':'8', '6':'9', '9':'6', '0': '0', '1':'1'}
  backwards_num = int("".join(reversed(str(n))))
  def is_prime(number):
    return not any((number % num == 0
                  for num in range(2, number//2 + 1,1)))
  if not is_prime(n):
    return 'C'
  elif n == backwards_num:
    return 'P'
  elif not is_prime(backwards_num):
    return 'P'
  elif all((num in flippable.keys() for num in str(n))):
    flipped_num = int("".join(flippable.get(num,'0') for num in str(backwards_num)))
    if is_prime(flipped_num) and is_prime(int("".join(reversed(str(flipped_num))))):  
      return 'B'
    return 'E'

