
d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
​
def eng2nums(s):
    l = s.split(' ')
    if len(l) == 1:
        return d[s]
    elif len(l) == 2:
        return d[l[0]]*100 if 'hundred' in l else d[l[0]] + d[l[1]]
    elif len(l) >= 3:
        return d[l[0]]*100 + eng2nums(' '.join(l[2:]))

