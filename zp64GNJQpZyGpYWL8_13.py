
def score_it(s):
    result, prod, number = 0, 0, ""
    for i in s:
        if not i.isnumeric():
            if number != "":
                result += prod*int(number)
                number = ""
        prod += (i == "(") - (i == ")")
        number += i if i.isnumeric() else ""
    return result

