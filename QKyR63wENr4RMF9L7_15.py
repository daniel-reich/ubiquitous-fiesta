
def tweak_letters(string, steps):
  return "".join([rotate(letter , value) for letter , value in zip(string,steps)]);
  
def rotate(letter , step):
  return "a" if (letter,step) == ("z" , 1)  else "z" if (letter , step) == ("a" ,-1) else chr(ord(letter) + step)

