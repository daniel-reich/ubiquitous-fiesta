
def sentence_primeness(sentence):
    satz = list(sentence)
    length = len(satz)
    n = 0
    woerter = []
    zahlen = []
    wort = ''
    summe = 0
    gesamt = 0
    while n < length: #get rid of spaces and symbols
        char = ord(satz[n])
        if char == 32 or char == 33 or char == 58 or char == 63 or char == 46:
            zahlen.append(summe)
            woerter.append(wort)
            summe = 0
            wort = ''
            n += 1
        elif 47 < char < 58:
            wort += chr(char)
            summe += (char-48)
            gesamt += (char-48)
            n += 1
        elif 64 < char < 91: 
            wort += chr(char)
            summe += (char-64)
            gesamt += (char-64)
            n += 1
        elif 96 < char < 123:
            wort += chr(char)
            summe += (char-96)
            gesamt += (char-96)
            n += 1
        else:
            n += 1
         
    if gesamt > 1: #check wether gesamt is a prime
        # Iterate from 2 to n / 2  
        for i in range(2, gesamt//2): 
         
        # If num is divisible by any number between  
        # 2 and n / 2, it is not prime  
            if (gesamt % i) == 0: 
                break
        else: 
            return('Prime Sentence')
    
    n = 0
    length = len(zahlen)
    while n < length:
        zahl = gesamt - zahlen[n]
        print(zahl)
        if zahl > 1:
            
            for i in range(2, zahl//2):
                if (zahl%i) == 0:
                    break
            else:
                return('Almost Prime Sentence (' + woerter[n] + ')')
        n += 1
    return('Composite Sentence')

