
def first_and_last(s):
  word = [i for i in s];
  word.sort();
  first="";
  last="";
  for i in range(len(word)):
    first+=word[i];
    
  for j in range(len(word)-1,-1,-1):
    last+=word[j];
    
  lex=[first,last];
  return lex;

