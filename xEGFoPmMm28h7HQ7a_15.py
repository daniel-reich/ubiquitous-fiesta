
def letter_combinations(digits):
    keys = {'1': '', '2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl', '6': 'mno', '7': 'prs', '8': 'tuv',
            '9': 'wxyz'}
    def permute(length):
        if length == len(digits):
            return list(keys[digits[len(digits)-1]])
        else:
            return [x + y for x in list(keys[digits[length - 1]]) for y in permute(length + 1)]
    return permute(1)

