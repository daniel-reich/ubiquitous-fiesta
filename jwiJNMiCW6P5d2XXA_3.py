
def does_rhyme(line1,line2):
    vowels = 'auioye'
    return [i.lower() for i in line1.split()[-1] if i.lower() in vowels] == \
               [i.lower() for i in line2.split()[-1] if i.lower() in vowels]

