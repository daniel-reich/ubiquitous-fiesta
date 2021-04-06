
import itertools
import copy
​
​
def letter_combinations(digits):
    digits_map = dict(zip(['2', '3', '4', '5', '6', '7', '8', '9'], ['abc', 'def', 'ghi', 'jkl', 'mno', 'prs', 'tuv', 'wxyz']))
    results = []
​
    for digit in digits[1:]:
        if not results:
            results = list(digits_map[digits[0]])
        old_results = copy.copy(results)
        results = []
        for combination in itertools.product(old_results, digits_map[digit]):
            results.append((''.join(combination)))
    return results

