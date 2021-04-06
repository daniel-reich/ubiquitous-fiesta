
def ascii_sort(arr):
        wrd1total = 0
        wrd2total = 0
        word1 = list(arr[0])
        word2 = list(arr[1])
        for ltr in word1:
                wrd1total += ord(ltr)
        for ltr in word2:
                wrd2total += ord(ltr)
        if wrd1total < wrd2total:
                return arr[0]
        else:
                return arr[1]

