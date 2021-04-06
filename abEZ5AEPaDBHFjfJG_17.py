
def formula(txt):
  if txt =='':
    return None
  else:
    if not 'a' in txt:
      txt = txt.split('=')
      #print(txt)
      res = eval(txt[0])
      bool = True
      for i in range(1,len(txt)):
        if res == eval(txt[i]):
          continue
        else:
          bool = False
          break
      return bool
    else:
      opr = ['*','+','-','/']
      if not any(elem in txt  for elem in opr):
        return True
      else:
        txt = txt.split('=')
        #print(txt)
        n = len(txt)
        res = 0
        i = 0
        bool = True
        while True:
          if not 'a' in txt[i]:
            res = eval(txt[i])
            break
          elif i + 1==n:
            break
          i+=1
        print(res)
        for i in range(n):
          if res == 0:
            break
          if 'a' in txt[i]:
            a = list(txt[i])
            if "*" in a:
              if res%int(a[-2])==0:
                bool = True
              else:
                bool = False
          elif res == eval(txt[i]):
            continue
          else:
            bool = False
            break
        return bool

