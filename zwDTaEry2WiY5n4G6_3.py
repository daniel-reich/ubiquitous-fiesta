
numbers={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
def digital_vowel_ban(number, word):
    b = list(str(number))
    c = [i for i in b if word not in numbers[i]]
    if c ==  []:
        return "Banned Number"
    else:
        return int("".join(c))

