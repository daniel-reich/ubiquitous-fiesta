
def letter_combinations(digits):
  def plc(dgts):
    dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    
​
    d = str(dgts)
​
    if len(d) == 3:
      poss = []
​
      firstlen = len(dic[d[0]])
      seconlen = len(dic[d[1]])
      thirdlen = len(dic[d[2]])
​
      
      possible_backs = []
      for n in range(3):
        for num in range(3):
          possible_backs.append(''.join([dic[d[1]][n], dic[d[2]][num]]))
     
      possible_backs = list(set(possible_backs))
      if firstlen == 4:
        for n in range(4):
          for back in possible_backs:
            poss.append(dic[d[0]][n] + back)
      else:
        
        for n in range(3):
          for back in possible_backs:
            poss.append(dic[d[0]][n] + back)
    
    elif len(d) == 2:
      poss = []
​
      for n in range(3):
        for num in range(3):
          poss.append(dic[d[0]][num] + dic[d[1]][n])
​
    return poss
  combs = plc(digits)
​
  return sorted(combs)

