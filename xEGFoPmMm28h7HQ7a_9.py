
from itertools import combinations
​
def letter_combinations (nums) :
  # my code is not very good
    '''input : a string of numbers
    output : all the letters possibly written with these numbers on a phone'''
    eq = {'2': list('abc'), '3': list('def'), '4':list('ghi'), '5': list('jkl'), '6': list('mno'), \
          '7': list('pqrs'), '8': list('tuv'), '9': list('wxyz')}
    possible = []
    for i in nums :
        for j in eq[i] :
            possible.append (j)
    sol = [''.join(i) for i in combinations (possible, len(nums)) if len(i) % len(nums) == 0]
    res = []
    banned = []
    for i in sol :
        for j in range (len(i)) :
            if i[j] in eq[nums[j]] :
                res.append (i)
            else :
                banned.append (i)
    return sorted(list(set([i for i in res if i not in banned])))

