
def translate_word(text):
    consonants = "B C D F G H J K L M N P Q R S T V W X Y Z".split(" ") 
    length = len(text)
    result = ""
    if length == 0:
        return result
    if text[0].isupper():
        upper_flag = True
    else:
        upper_flag = False
    if text[0].upper() not in consonants:
        result = text + "yay"
    else:
        for i in range(length):
            upper = text[i].upper()
            if upper in consonants:
                if i == 0 and upper_flag:
                    result = result + text[i].lower()
                else:
                    result = result + text[i]
            else:
                #print(result, text[i:])
                result =  text[i:]+ result +"ay"
                break
    if upper_flag:
        temp_result = result
        result = result[0].upper() + temp_result[1:]
        
    return result
​
import re
def translate_sentence(text):
    new_text = re.sub(r'[A-Za-z]+', lambda x: translate_word(x.group()), text)
    return new_text

