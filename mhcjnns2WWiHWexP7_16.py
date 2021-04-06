
def calculate_arrowhead(lst):
    if isinstance(lst, list):
        #print("Het is een list")
        pass
    else:
        print("het is geen list, maar een {}".format(type(lst)))
    aantal_zetten = len(lst)
    #print("aantal zetten is {}".format(aantal_zetten))
​
    verplaatsing = 0
    for zet in lst:
        #print(zet)
        if '<' in zet:
            #print("Links")
            verplaatsing -= len(zet)
        elif '>' in zet:
            #print("Rechts")
            verplaatsing += len(zet)
        else:
            print("Foute input!")
    
    #print("De verplaatsing is {}".format(verplaatsing))
    if verplaatsing < 0:
        visueel = abs(verplaatsing) * '<'
        #print("Links")
    elif verplaatsing > 0:
        #print("Rechts")
        visueel = verplaatsing * '>'
    elif verplaatsing == 0:
        #print("Blijf staan...")
        visueel = ''
    return visueel

