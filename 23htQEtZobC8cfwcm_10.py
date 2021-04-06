
def canConcatenate(arr, arr2):
    saida = []
    for i in arr:
        saida.extend(i)
    saida.sort()
    arr2.sort()
    return saida == arr2

