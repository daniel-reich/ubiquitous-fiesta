
def ruth_aaron(a):
  arepeating = []
  anonrepeating = set()
  b = a
  while b != 1:
    for i in range(2, b + 1):
      if b % i == 0:
        factors = 0
        for j in range(2, i):
          if i % j == 0:
            factors += 1
        if factors == 0:
          arepeating.append(i)
          anonrepeating.add(i)
          b = int(b/i)
  arepeating.sort()
  arsum = 0
  anrsum = 0
  for i in arepeating:
    arsum += i
  for i in anonrepeating:
    anrsum += i
  result = []
  success = 0
  crepeating = []
  cnonrepeating = set()
  b = a -1
  while b != 1:
    for i in range(2, b + 1):
      if b % i == 0:
        factors = 0
        for j in range(2, i):
          if i % j == 0:
            factors += 1
        if factors == 0:
          crepeating.append(i)
          cnonrepeating.add(i)
          b = int(b/i)
  crepeating.sort()
  crsum = 0
  cnrsum = 0
  for i in crepeating:
    crsum += i
  for i in cnonrepeating:
    cnrsum += i
  if arsum == crsum and anrsum == cnrsum:
    return(['Aaron',3])
  elif arsum == crsum:
    return(['Aaron',2])
  elif anrsum == cnrsum:
    return(['Aaron',1])
  else:
    success +=1
  erepeating = []
  enonrepeating = set()
  b = a + 1
  while b != 1:
    for i in range(2, b + 1):
      if b % i == 0:
        factors = 0
        for j in range(2, i):
          if i % j == 0:
            factors += 1
        if factors == 0:
          erepeating.append(i)
          enonrepeating.add(i)
          b = int(b/i)
  erepeating.sort()
  ersum = 0
  enrsum = 0
  for i in erepeating:
    ersum += i
  for i in enonrepeating:
    enrsum += i
​
  if arsum == ersum and anrsum == enrsum:
    return(['Ruth',3])
  elif arsum == ersum:
    return(['Ruth',2])
  elif anrsum == enrsum:
    return(['Ruth',1])
  elif success == 1:
    return(1==0)

