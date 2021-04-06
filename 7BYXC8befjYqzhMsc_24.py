
def classify_rug(arr):
    horizontal = True
    vertical = True
    # sudah pasti perfect jika 1x1
    if len(arr) == 1 and len(arr[0]) == 1:
        return "perfect"
​
    isi_ver = [""] * len(arr)
    isi_hor = [""] * len(arr[0])
​
    # looping untuk verti
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            isi_ver[x] += arr[x][y]
        # cek si vertical
        if isi_ver[x] != isi_ver[x][::-1]:
            vertical = False
​
    # looping untuk hori
    for y in range(len(arr[0])):
        for x in range(len(arr)):
            isi_hor[y] += arr[x][y]
        # cek si hori
        if isi_hor[y] != isi_hor[y][::-1]:
            horizontal = False
​
    if horizontal == True and vertical == False:
        return "horizontally symmetric"
    elif horizontal == False and vertical == True:
        return "vertically symmetric"
    elif horizontal and vertical:
        return "perfect"
    else:
        return "imperfect"
​
print(classify_rug([
    ["a", "a", "a", "a"],
    ["d", "a", "a", "a"],
]))

