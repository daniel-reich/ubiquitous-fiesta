
d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
     "7": "pqrs", "8": "tuv", "9": "wxyz"}
def letters_combinations(digits):
    vars, fors = [], []
    for i, digit in enumerate(digits):
        vars.append("x{}".format(i))
        fors.append("for {} in \"{}\"".format(vars[-1], d[digit]))
    return eval("set({} {})".format("+".join(vars), " ".join(fors)))

