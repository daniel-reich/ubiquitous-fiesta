
def dif_ciph(impt):
  if (isinstance(impt , str)):
    return encode(impt);
  elif (all([isinstance(num , int) for num in impt])):
    return decode(impt);
    
def encode(string):
  return [ord(string[0])] + [ ord(b) - ord(a) for a ,b in zip(string, string[1:])];
​
def decode(nums):
  return "".join([chr(sum(nums[:idx])) for idx in range(1 , len(nums)+1)]);

