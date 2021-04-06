
def get_languages(num):
    dict_1={'1':'C#','2':'C++','4':'Java',
        '8':'JavaScript','16':'PHP','32':'Python',
        '64':'Ruby','128':'Swift'}
    array=[128,64,32,16,8,4,2,1]
    array_2=[]
    for x in range(len(array)):
        if(array[x]<=num):
            num^=array[x]
            array_2.append(array[x])
    array_2.sort()
    for z in range(len(array_2)):
        array_2[z]=dict_1[str(array_2[z])]
    return array_2

