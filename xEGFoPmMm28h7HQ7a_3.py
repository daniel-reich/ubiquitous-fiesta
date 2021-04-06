
import itertools
def letter_combinations(digits):
  phoneDict = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno',
         '7':'pqrs', '8':'tuv', '9':'wxyz'}
  lst = [phoneDict[i] for i in digits]
  return [''.join(i) for i in itertools.product(*lst)]

