
def uncensor(txt, vowels):
    lst = [a +b for a, b in zip(txt.split('*'), list(vowels))]+ txt.split('*')[-1:]
    return ''.join(lst)

