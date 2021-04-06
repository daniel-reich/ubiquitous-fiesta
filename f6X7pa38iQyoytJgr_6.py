
def increasing_word_weights(sentence):
    for i in sentence:
        if not i.isspace() and not i.isalnum():
            sentence = sentence.replace(i, "")
    s = sentence.split()
    arr = []
    for i in range(len(s)):
        arr.append([])
        for x in range(len(s[i])):
            while len(arr[i]) <= len(s[i]):
                arr[i].append(ord(s[i][x]))
                break
    for i in range(len(arr)):
        arr[i] = sum(arr[i])
​
    return sorted(arr) == arr

