
def count_digits(lst, t):
    lista = []
    listeven= []
    listodd = []
    nlisteven = []
    nlistodd = []
    for num in lst:
        lista.append(list(str(num)))
    for l in lista:
        listeven.append([1 for n in l if int(n) % 2 == 0])
        listodd.append([1 for n in l if int(n) % 2 == 1])
    for li in listeven:
        nlisteven.append(sum(li))
    for li in listodd:
        nlistodd.append(sum(li))
    if t == "even":
        return nlisteven
    return nlistodd

