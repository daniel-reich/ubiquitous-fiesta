
def dakiti(sentence):
    started_list = sentence.split(' ')
    orded_list = []
    numbers = []
    for item in started_list:
        for number in item:
            if number.isdigit():
                numbers.append(number)
    numbers.sort()
    for loop in numbers:
        for item in started_list: 
            if loop in item:
                fitem = item.replace(loop,'')
                orded_list.append(fitem)
    final = ''
    for item in orded_list:
        final += item
        final += ' '
    return final[:-1]

