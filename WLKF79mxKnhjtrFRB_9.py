
def is_good_match(lst):
    if len(lst) % 2 != 0:
        return "bad match"
    married = []
    while lst:
        num1 = lst.pop(0)
        num2 = lst.pop(0)
        married.append(num1 + num2)
    return married

