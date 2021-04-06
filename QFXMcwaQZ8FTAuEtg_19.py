
def counterpartCharCode(char):
​
    if char == char.lower():
        return ord(char.upper())
​
    if char == char.upper():
        return ord(char.lower())

