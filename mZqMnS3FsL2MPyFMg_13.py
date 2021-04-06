
numbers = {
0: "zero",
1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eigth",
9: "nine",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifeteen",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen",
20: "twenty",
30: "thirty",
50: "fifty"
}
def num_to_eng(n):
  res = ""
  if n in numbers.keys():
    return numbers[n]
  if n >= 100:
    res = numbers[n//100] + " hundred" + " "
    n = n % 100
  if n in numbers.keys():
    return res + numbers[n]
  p = (n // 10)*10 
  if p in numbers.keys():
    res += numbers[p]
  else:
    res += numbers[n // 10] + "ty"
  return res + " " + numbers[n-p]   
    
  
  return res

