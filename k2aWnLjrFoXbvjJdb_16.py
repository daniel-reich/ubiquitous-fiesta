
import string
def vigenere(text, keyword):
  alphabet = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
  alphabet1=[]
  which=[0 if (text[i]==text[i].upper() and not text[i]==' ' and not text[i]==string.punctuation) else 1 for i in range(len(text))]
  for i in range(len(alphabet)):
    alphabet1.append(alphabet[i:len(alphabet)] + alphabet[0:i])
  exclude_list = string.punctuation + ' '
  table = str.maketrans(exclude_list, len(exclude_list) * " ")
  s1=''.join(text.upper().translate(table).split())
  s2=''.join(keyword.upper().translate(table).split())
  s2_t= ''.join([s2[i%len(s2)] for i in range(len(s1))])
  if not (sum(which)==0):
    return(''.join([alphabet1[alphabet.index(s1[i])][alphabet.index(s2_t[i])] for i in range(len(s1))]))
  else:
    return (''.join([alphabet[alphabet1[alphabet.index(s2_t[i])].index(s1[i])] for i in range (len(s1))]))

