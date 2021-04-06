
def eng2nums(number):
​
  numberdict = {"zero": 0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, 
        "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fiteen":15, "sixteen":16, "seventeen":17,
        "eighteen":18, "nineteen":19, "twenty":20, "thirty": 30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90,
        "hundred": 100}
​
  split_number = number.split(" ")
  
  if len(split_number) > 1:
    if split_number[1] == "hundred":
      hundred = numberdict[split_number[0]]
      split_number = split_number[2:]
​
      total = hundred * 100
      # print(total)
      # print(split_number)
      for n in split_number:
        # print(n)
        total += numberdict[n]
​
      return total
    else:
      total = 0
      for n in split_number:
        # print(n)
        total += numberdict[n]
​
      return total
    
    
  else:
​
    return numberdict[number]

