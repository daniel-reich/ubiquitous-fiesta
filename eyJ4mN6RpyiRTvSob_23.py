
def is_palindrome_possible(STR1: str):
    STR_LST = list(STR1)
    AorB =  [str(STR1.count(i) % 2) for i in STR_LST]
    Zero_and_Ones = [AorB.count(i) for i in ['0','1']]
    return True if Zero_and_Ones[0] % 2 == 0 and Zero_and_Ones[1] in [0, 1] else False

