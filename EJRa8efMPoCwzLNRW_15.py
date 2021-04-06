
import re
​
def dakiti(sentence):
    words = sentence.split(' ')
    numbers = [re.findall(r'[0-9]',word) for word in words]
    output_sequence = [None for x in range(len(numbers))]
    for index,word in enumerate(words):
        output_sequence[int(numbers[index][0])-1] = re.sub('\\d','',words[index])
    return ' '.join(output_sequence)

