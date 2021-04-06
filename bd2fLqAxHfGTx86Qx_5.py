
def can_complete(word: str, txt: str) -> bool:
    index = 0
    for i in word:
        temp = txt[index:].find(i)
        print(temp, txt[index:])
        if temp != -1:
            index += temp + 1
        else:
            return False
    return True

