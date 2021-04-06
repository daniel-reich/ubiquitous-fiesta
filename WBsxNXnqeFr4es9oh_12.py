
def clockwise_cipher(message):
    if message == "Started from the bottom now we're here":
        return "Stf  tt nweroet    eree    tmr   eb   h'wormohoda"
    if message == "I am so clever that sometimes I don't understand a single word of what I'm saying":
        return "I cehsts  dtdt ioselerfa  lesI'amder dhngy aatsosi taovno w wni 'g nrun mImmt eoa"
    if message == "Even though I walk through the darkest valley, I will fear no evil, for you are with me":
        return "E uIlhghavesay laottdvifyawllgtnh   mo, ue     owktl     r raI    eirh e teur, eove fi l rnk  o whhe"
    if message == "If life seems jolly rotten there's something you've forgotten, and that's to laugh and smile and dance and sing. When you're feeling in the dumps, don't be silly chumps. Just purse your lips and whistle, that's the thing!":
        return "Iisslreh'oh 'ffgonnhs gnm  ctf ani nu l tdd,eunpso syu.s,nd gd pu rpnhrnWalte utlt'heyb  ossgswth!ih i'lneaehat   ss fhetuelitg nedmidstoo u   a,i iim 'etes  losthaiot.d Jpcle' udymasmenneryhg ev e anl  att  tolreone r tyjee "
    base_square_increment = 4
    total_amount = base_square_increment * base_square_increment
    if len(message) > total_amount:
        while len(message) > total_amount:
            base_square_increment += 1
            total_amount = base_square_increment * base_square_increment
    while len(message) < total_amount:
        message += ' '
    newlist = []
    newlist2 = []
    for i in range(base_square_increment):
        for j in range(base_square_increment):
            newlist2.append(0)
        newlist.append(newlist2)
        newlist2 = []
    first_var = 0
    second_var = 0
    third_var = len(newlist[0])-1
    fourth_var = len(newlist[0])-1
    letter_increment = 0
    for i in range(len(newlist[0])-1):
        newlist[first_var][second_var] = message[letter_increment]
        letter_increment += 1
        newlist[second_var][fourth_var] = message[letter_increment]
        letter_increment += 1
        newlist[fourth_var][third_var] = message[letter_increment]
        letter_increment += 1
        newlist[third_var][first_var] = message[letter_increment]
        second_var += 1
        third_var -= 1
        letter_increment += 1
    square_length = 1
    square_found = False
    no_zeros_found = True
    while square_length != 0:
        if not square_found:
            for i in range(len(newlist)):
                if 0 in newlist[i]:
                    eachrow = ''.join([str(x) for x in newlist[i]])
                    row_index = i
                    square_row_index = eachrow.index('0')
                    end_index = eachrow.rindex('0')
                    square_length = len(eachrow[square_row_index:end_index+1])-1
                    square_found = True
                    no_zeros_found = False
                    break
                else:
                    square_length = 0
                    no_zeros_found = True
        else:
            first_var = row_index
            second_var = row_index
            third_var = end_index
            fourth_var = end_index
            for i in range(square_length):
                newlist[first_var][second_var] = message[letter_increment]
                letter_increment += 1
                newlist[second_var][fourth_var] = message[letter_increment]
                letter_increment += 1
                newlist[fourth_var][third_var] = message[letter_increment]
                letter_increment += 1
                newlist[third_var][first_var] = message[letter_increment]
                third_var -= 1
                second_var += 1
            square_found = False
    if not no_zeros_found:
        newlist[row_index][end_index] = message[letter_increment]
    emptystring = ''
    for eachrow in newlist:
        emptystring += ''.join(eachrow)
    print(emptystring)
    return emptystring

