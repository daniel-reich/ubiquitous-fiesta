
def is_untouchable(n):
  if(n >= 2):
    a = [i for i in range(2, n**2 + 1)
        if (1 + sum(sum({j, i // j}) for j in range(2, int(i ** 0.5) + 1)
                if not i % j)) == n]
    return a if len(a) > 0 else True
  else:
    return 'Invalid Input'

