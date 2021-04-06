
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    play_A = [ord(letter) for i, letter in enumerate(str_A)
             if i not in ind_Z]
    play_Z = [ord(letter) for i, letter in enumerate(str_Z)
             if i not in ind_A]
    scoring = [(A-Z, Z-A) for A, Z in zip(play_A, play_Z)]
    result = {
        'A': sum([s[0] for s in scoring if s[0] > 0]),
        'Z': sum([s[1] for s in scoring if s[1] > 0])
    }
    return result

