
def num_to_eng(n):
  single = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]
  if n < 10:
    return single[n]
  if n < 20:
    return teen[n-10]
  if n < 100:
    if n %10 == 0:
      return tens[n//10 - 2]
    return tens[n//10 -2] + " " + single[n%10]
  if n % 100 == 0:
    return single[n//100] + " " + "hundred"
  return single[n//100] + " " + "hundred " + num_to_eng(n%100)

