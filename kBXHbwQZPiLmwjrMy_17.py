
import re
​
def translate_word(word):
  vowels=['a','e','i','o','u']
  upper=False
  if len(word)==0:
    return word
  else:
    if word[0].isalpha() and word[0].lower() in vowels:
      word+='yay'
    else:
      word1=''
      for i in range (0,len(word)):
        if not (word[i].lower() in vowels):
          if (i==0 and word[i].upper()==word[i]):
            upper=True
          word1+=word[i].lower()
        else:
          if upper:
            word=word[i].upper()+word[min(i+1,len(word)):]+word1 +'ay'
          else:
            word=word[i:]+word1 +'ay'
          break
    return word 
​
def translate_sentence(sentence):
  out, i='',0
  lst=re.findall(r"[A-Za-z@#]+|.", sentence)
  for i in range (len(lst)):
    if(lst[i].isalpha()):
      out+=translate_word(lst[i])
    else:
      out+=lst[i]
  return out

