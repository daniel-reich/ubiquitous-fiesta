
def isWordChain(words):
  def change(sword, eword):
​
    slist = list(sword)
    elist = list(eword)
​
    changed = 0
    
    for n in range(0, len(slist)):
​
      sl8r = slist[n]
      el8r = elist[n]
​
      if sl8r != el8r:
        changed += 1
    
    if changed > 1:
      return False
    elif changed < 1:
      return False
    else:
      return True
  def add_sub(sword, eword):
    
    slist = list(sword)
    elist = list(eword)
​
    slen = len(slist)
    elen = len(elist)
​
    if elen == slen + 1:
      return True
    elif elen == slen - 1:
      p = True
      ns = []
      for l8r in elist:
        
        for n in range(0, len(slist)):
          sl8r = slist[n]
​
          if sl8r == l8r:
            ns.append(n)
        
      sns = sorted(ns)
      stdword = ''
      
      for item in sns:
        l8r = slist[item]
        stdword += l8r
      
      if ns == sns and stdword == eword:
        return True
      else:
        return False
    else:
      return False
​
  possible = True
​
  n = 0
​
  while possible == True:
​
    word1 = words[n]
    try:
      word2 = words[n + 1]
    except IndexError:
      return possible
    
    list1 = list(word1)
    list2 = list(word2)
​
    len1 = len(list1)
    len2 = len(list2)
​
    if len1 == len2:
      possible = change(word1, word2)
    else:
      possible = add_sub(word1, word2)
​
    n += 1
​
  return possible

