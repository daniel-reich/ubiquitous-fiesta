
import itertools
num_ltrs = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
def letter_combinations(digits):
  return list(map(''.join,itertools.product(*[num_ltrs[int(d)] for d in digits])))

