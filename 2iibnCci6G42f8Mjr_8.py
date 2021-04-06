
def guess_score(code, guess):
    dct = {"black": 0, "white": 0}
    arr_code = []
    arr_guess = []
    for x in range(len(code)):
        arr_code.append(code[x])
        arr_guess.append(guess[x])
    
    count = 0
    for i in range(len(code)):
        if code[i] == guess[i]:
            count += 1
            arr_code.pop(i)
            arr_guess.pop(i)
    
    dct['black'] = count
    count = 0
    for i in arr_code:
        if i in arr_guess:
            count += 1
            arr_guess.pop(arr_guess.index(i))
    
    dct['white'] = count
    return dct

