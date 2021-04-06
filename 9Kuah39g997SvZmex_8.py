
def common_last_vowel(txt):
    string_2=txt.replace("!","").replace(",","").replace(".","")
    string_3=string_2.lower()
    array=string_3.split(" ")
    array_2=['a','e','i','o','u']
    count_1=0
    count_2=0
    count_3=0
    count_4=0
    count_5=0
    for x in range(len(array)):
        if(array[x].endswith('a')):
            count_1+=1
        if(array[x].endswith('e')):
            count_2+=1
        if(array[x].endswith('i')):
            count_3+=1
        if(array[x].endswith('o')):
            count_4+=1
        if(array[x].endswith('u')):
            count_5+=1
    for x in range(len(array)):
        for z in range(len(array[x])):
            for q in range(len(array_2)):
                if(array[x][z]==array_2[q]):
                    if(array_2[q]==array_2[0]):
                        count_1+=1
                    if(array_2[q]==array_2[1]):
                        count_2+=1
                    if(array_2[q]==array_2[2]):
                        count_3+=1
                    if(array_2[q]==array_2[3]):
                        count_4+=1
                    if(array_2[q]==array_2[4]):
                        count_5+=1
                    
    if(count_5>count_4 and count_5>count_3 and count_5>count_2 and count_5>count_1):
        return array_2[4]
    if(count_4>count_5 and count_4>count_3 and count_4>count_2 and count_4>count_1):
        return array_2[3]
    if(count_3>count_4 and count_3>count_5 and count_3>count_2 and count_3>count_1):
        return array_2[2]
    if(count_2>count_4 and count_2>count_3 and count_2>count_5 and count_2>count_1):
        return array_2[1]
    if(count_1>count_4 and count_1>count_3 and count_1>count_2 and count_1>count_5):
        return array_2[0]

