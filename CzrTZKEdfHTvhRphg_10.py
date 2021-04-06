
def mixed_number(frac): 
    bruch = list(frac)
    length = len(bruch)
    n = 0
    num1 = ""
    num2 = ""
    nummer = ''
    negativ = ''
    while n < length: #get both numbers
        char = bruch[n]
        if char == '-':
            negativ = char
        elif 47 < ord(char) < 58:
            nummer += char
        else:
            num1 = nummer
            nummer = ''
        n += 1
    num2 = nummer
    num1 = int(num1) #string to int
    num2 = int(num2) #string to int
    
    if (num1 / num2) > 1: #vereinfachen
        zaehler = (num1 % num2)
        zahl = (num1-zaehler)/num2
    else:
        zaehler = num1
        zahl = 0
    
    nenner = num2
    
    if zaehler == 0:
        return(negativ+str(round(zahl)))
    else:
        n = (zaehler)
        while  n > 0:
            if zaehler%n == 0 and nenner%n == 0:
                zaehler = zaehler/n
                nenner = nenner/n
                n = n-1
            else:
                n = n-1
        if zahl == 0:
            string = ''
            string = negativ+str(round(zaehler))+'/'+str(round(nenner))
            return(string)
        else:
            string = ''
            string = negativ+str(round(zahl))+' '+str(round(zaehler))+'/'+str(round(nenner))
            return(string)

