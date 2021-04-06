
def num_to_eng(n):
​
  one_2_twenty = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'}
​
  twentyone_to_ninetynine = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
​
  hundreds = {1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred', 5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'}
​
  if n <= 20:
    return one_2_twenty[n]
  elif n > 20 and n <= 99:
    
    l = list(str(n))
​
    parts = [twentyone_to_ninetynine[int(l[0])], one_2_twenty[int(l[1])]]
​
    return ' '.join(parts)
​
  elif n > 99 and n <= 999:
​
    l = list(str(n))
​
    parts = [hundreds[int(l[0])]]
​
    test = int('{o}{t}'.format(o = l[1], t = l[2]))
​
    if test in one_2_twenty:
      parts.append(one_2_twenty[test])
    else:
      parts.append(twentyone_to_ninetynine[int(l[1])])
      parts.append(one_2_twenty[int(l[2])])
​
    return ' '.join(parts)

