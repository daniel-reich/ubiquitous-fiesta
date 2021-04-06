
def is_disarium(n):
    t = 0
    n = list(str(n))
    for i in range(len(n)):
      t = t + int(n[i])**(i+1)
    return int(''.join(n)) == t

