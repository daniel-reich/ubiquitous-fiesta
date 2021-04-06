
def describe_num(n):
​
  dct = { 1 : "brilliant",
      2 : "exciting",
      3 : "fantastic",
      4 : "virtuous",
      5 : "heart-warming",
      6 : "tear-jerking",
      7 : "beautiful",
      8 : "exhilarating",
      9 : "emotional",
      10 : "inspiring"
      }
​
  factors = [dct.get(i) for i in range(1, 11) if n%i == 0]
  
  string = " ".join(factors)
​
  return "The most {} number is {}!".format(string, n)

