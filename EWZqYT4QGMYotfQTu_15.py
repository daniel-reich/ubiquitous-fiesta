
dic = {"a": (1,1), "b": (1,2), "c": (1,3), "d": (1,4), "e": (1,5), 
       "f": (2,1), "g": (2,2), "h": (2,3), "i": (2,4), "j": (2,5),
       "k": (1,3), 
       "l": (3,1), "m": (3,2), "n": (3,3), "o": (3,4), "p": (3,5),
       "q": (4,1), "r": (4,2), "s": (4,3), "t": (4,4), "u": (4,5),
       "v": (5,1), "w": (5,2), "x": (5,3), "y": (5,4), "z": (5,5)}
rdic = {v: k for k,v in dic.items()}
rdic[(1,3)] = "c"
​
def tap_code(text):
  if "." in text:
    ret = []
    words = text.split(" ")
    for i in range(len(words)//2):
      a, b = len(words[2*i]), len(words[2*i+1])
      ret.append(rdic[(a,b)])
    return "".join(ret)
  else:
    ret = []
    for c in text:
      a, b = dic[c]
      ret.append("."*a + " " + "."*b)
    return " ".join(ret)

