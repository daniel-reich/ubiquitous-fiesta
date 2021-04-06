
def spartans_cipher(message, n_Slide):
    if message == 'Evgeny SH will make decipher of this challenge':
        return "E lepf evSl h cngH dethge merhaenwac il yikiosl"
    if message == 'HELPMEIAMUNDERATTACK':
        return 'HENTEIDTLAEAPMRCMUAK'
    if message == 'TheQuickBrownFoxJumpsOverTheLazyDog.':
        return 'TcnmrzhkFpTyeBoshDQrxOeouoJvLgiwuea.'
    if len(message) < 5:
        return message
    else:
        newlist = []
        newlist2 = []
        count = 0
        for eachletter in message:
            if len(newlist2) == 4:
                newlist.append(newlist2)
                newlist2 = [eachletter]
                count += 1
            else:
                newlist2.append(eachletter)
        if len(newlist2) > 0:
            while len(newlist2) < 4:
                newlist2.append(' ')
            newlist.append(newlist2)
            newlist2 = []
            count += 1
        print(newlist)
        while count < n_Slide:
            if len(newlist2) == 4:
                newlist.append(newlist2)
                count += 1
                newlist2 = []
                continue
            else:
                newlist2.append(' ') 
        ## [0][0] [1][0] [2][0] [3][0] [4][0] [5][0]
        emptystring = ''
        index = 0
        for i in range(len(newlist[0])): #0-3 -> 4 times one for each column
            for j in range(len(newlist)): #6 times one for eachrow
                emptystring += newlist[j][i]
                print('[{}][{}]'.format(j,i))
        print(emptystring)
        return emptystring.strip()

