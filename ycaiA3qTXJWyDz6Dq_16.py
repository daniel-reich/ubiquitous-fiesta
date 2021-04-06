
import re
​
def consonants(word):
    container = 0
    pattern = re.compile('[^AEIOUaieou0-9\s\W]')
    data = pattern.finditer(word)
    for i in data:
        container += 1
​
    return container
​
​
def vowels(word):
​
​
        container = 0
        pattern = re.compile('[AEIOUaieou]')
        data = pattern.finditer(word)
        for i in data:
            container += 1
        return container

