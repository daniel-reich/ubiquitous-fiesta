
import re
​
​
def mystery_func ( txt ):
    line = ""
    index = 0
    numbers = re.findall("[0-9]", txt)
    letters = re.findall("[^0-9]", txt)
    for number in numbers:
        for num in range(int(number)):
            line += letters[index]
        index += 1
    return line

