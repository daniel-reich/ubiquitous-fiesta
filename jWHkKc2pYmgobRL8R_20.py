
def distance_to_nearest_vowel(txt):
    vowels=['a','e','i','o','u']
    position=[]
    place=0
    if len(txt)==0:
        print("No text was submitted.")
    else:
        for i in txt:
            place+=1
            for j in vowels:
                if i==j:
                    position.append(place-1) 
    if len(position)==0:
        print('There were no vowels in submitted text')
    else:
        finalpos=[]
        for i in range(0,len(txt)):
            relpos=[]
            for j in position:
                relpos.append(abs(i-j))
            relpos.sort()
            finalpos.append(relpos[0])
    return finalpos

