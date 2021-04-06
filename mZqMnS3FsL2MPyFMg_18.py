
def num_to_eng(n):
  numwords = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety'}
  if n in numwords:
    return numwords[n]
  else:
    out = []
    if n//100 > 0:
      out.append("{} hundred".format(numwords[n//100]))
    n %= 100
    if n in numwords:
      out.append("{}".format(numwords[n]))
    else:
      if (n-(n%10)) > 0:
        out.append("{}".format(numwords[n-(n%10)]))
      if (n%10) > 0:
        out.append("{}".format(numwords[n%10]))
    return " ".join(out)

