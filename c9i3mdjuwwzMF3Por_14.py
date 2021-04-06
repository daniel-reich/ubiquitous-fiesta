
def bemirp(n):
  s = str(n)
  upside_down = ['6x' if i == '9' else i for i in s]
  upside_down = ['9' if i == '6' else i for i in upside_down]
  upside_down = int(''.join(['6' if i == '6x' else i for i in upside_down]))
  reversed_upside_down = int(str(upside_down)[::-1])
  def is_prime(num):
      for i in range(2,num//2+1):
          if num%i == 0:
              return 'C'
      else:
          return 'P'
​
  if is_prime(n) == 'C':
      return 'C'
  elif int(s[::-1]) != n and is_prime(int(s[::-1])) == 'P':
      num_stat = 'E'
  else:
      num_stat = 'P'
  if len([i for i in s if not i in ('0','1','6','8','9')]) > 0:
      return num_stat
  else:
      if is_prime(upside_down) == 'P' and is_prime(reversed_upside_down == 'P') and upside_down != reversed_upside_down:
          return 'B'
      else:
          return num_stat

