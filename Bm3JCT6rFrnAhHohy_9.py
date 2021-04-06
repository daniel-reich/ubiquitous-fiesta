
import string
​
string = string.ascii_lowercase
​
def alphabet_index(str1):
    return " ".join(list(map(str,[string.index(char)+1 for char in str1.lower() if char in string])))

