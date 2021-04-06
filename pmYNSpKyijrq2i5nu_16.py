
from itertools import product
def darts_solver(sections, darts, target):
  testlist = []
  finallist = []
  fulllist = list(product(sections,repeat=darts))
  for rawitem in fulllist:
    item = []
    for a in rawitem:
      item.append(a)
    numbertotal = 0
    for number in item:
      numbertotal = numbertotal + number
    if numbertotal == target:
      testresult = False
      for a in testlist:
        a.sort()
        item.sort()
        if item == a:
          testresult = True
      if testresult == False:
        finalitem = ""
        rotation = 0
        for a in item:
          finalitem = finalitem + str(a)
          if rotation < len(item)-1:
            finalitem = finalitem + "-"
          rotation += 1
        finallist.append(finalitem)
        testlist.append(item)
    
  print(finallist)  
  
  return finallist

