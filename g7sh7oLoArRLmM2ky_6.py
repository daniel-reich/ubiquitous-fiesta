
import re
def baconify(msg, mask=""):
​
    d_key={
  "uuuuu"  :"a" ,
  "uuuul"  :"b" ,
  "uuulu"  :"c" ,
  "uuull"  :"d" ,
  "uuluu"  :"e" ,
  "uulul"  :"f" ,
  "uullu"  :"g" ,
  "uulll"  :"h" ,
  "uluuu"  :"i" ,
  "uluul"  :"j" ,
  "ululu"  :"k" ,
  "ulull"  :"l" ,
  "ulluu"  :"m" ,
  "ullul"  :"n" ,
  "ulllu"  :"o" ,
  "ullll"  :"p" ,
  "luuuu"  :"q" ,
  "luuul"  :"r" ,
  "luulu"  :"s" ,
  "luull"  :"t" ,
  "luluu"  :"u" ,
  "lulul"  :"v" ,
  "lullu"  :"w" ,
  "lulll"  :"x" ,
  "lluuu"  :"y" ,
  "lluul"  :"z" ,
  "llllu"  :"." ,
  "lllll"  :" " 
  }
​
    e_key={
    "a": "uuuuu",
    "b": "uuuul",
    "c": "uuulu",
    "d": "uuull",
    "e": "uuluu",
    "f": "uulul",
    "g": "uullu",
    "h": "uulll",
    "i": "uluuu",
    "j": "uluul",
    "k": "ululu",
    "l": "ulull",
    "m": "ulluu",
    "n": "ullul",
    "o": "ulllu",
    "p": "ullll",
    "q": "luuuu",
    "r": "luuul",
    "s": "luulu",
    "t": "luull",
    "u": "luluu",
    "v": "lulul",
    "w": "lullu",
    "x": "lulll",
    "y": "lluuu",
    "z": "lluul",
    ".": "llllu",
    " ": "lllll"
  }
​
    return_statement=""
    borken_word=""
    if not mask:
        msg=re.sub("[\d\W\s]","",msg)
        for ch in msg:
            borken_word+="l" if str.islower(ch) else "u"
            if len(borken_word)==5:
                return_statement+=(d_key[borken_word])
                borken_word=""
        return return_statement
            
    else:
        ch_count=0
        msg= re.sub("[!?:;'\"]","",msg)
        return_statement=list(mask)
        for ch in str.lower(msg):
            for x in (e_key[ch]):
                while not str.isalpha(mask[ch_count]):
                    ch_count+=1
                return_statement[ch_count]=str.upper(mask[ch_count]) if x=="u" else str.lower(mask[ch_count])
                ch_count+=1 
        return "".join(return_statement)

