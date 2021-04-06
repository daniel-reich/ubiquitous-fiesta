
def max_score(s):
  return max([len([1 for i in s[:j] if i == '0'] 
                + [1 for i in s[j:] if i == '1'])
              for j in range(1,len(s))])

