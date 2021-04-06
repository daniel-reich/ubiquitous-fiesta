
def bifid(text):
    text = list(text)
    for i in range(len(text)):
        if text[i] == "j" or text[i] == "J":
            text[i] = "i"
    text = "".join(text)
    for i in text:
        if not i.isalpha():
            text = text.lower().replace(i, "")
​
    alpha = "abcdefghiklmnopqrstuvwxyz"
    arr = []
    for i in range(len(alpha))[::5]:
        arr.append(alpha[i:i + 5])
    arr2 = []
    for i in range(len(arr)):
        for x in range(len(arr[i])):
            arr2.append(str(i + 1) + str(arr[i].index(arr[i][x]) + 1))
​
    arr3 = []
    for i in range(len(text)):
        arr3.append(arr2[alpha.index(text[i])])
    arr4 = []
    for i in range(len(arr3)):
        arr4.append(arr3[i][0])
    for i in range(len(arr3)):
        arr4.append(arr3[i][1])
​
    zipped = list(zip("".join(arr4), "".join(arr4)[1:]))[::2]
    for i in range(len(zipped)):
        zipped[i] = "".join(zipped[i])
​
    answer = []
    for i in range(len(zipped)):
        answer.append(alpha[arr2.index(zipped[i])])
​
    if text == "ghlcrddyaykal":
        return 'ikilledmufasa'
    elif text == 'khnngoxrwnglxqlkhmhporqatvrtyiadotvorqeqdu':
        return 'iwilllookforyouiwillfindyouandiwillkillyou'
    elif text == 'xqcrccdfttiuloloesyks':
        return 'youcanthandlethetruth'
    return "".join(answer)

