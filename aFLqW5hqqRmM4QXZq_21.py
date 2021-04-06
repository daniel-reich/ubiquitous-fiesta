
def bar_chart(results):
    key = []
    value = []
    isi = ""
    for i in results.items():
        key += [i[0]]
        value += [i[1]]
  
    for i in range(len(key)):
        for j in range(len(key)-i-1):
            if value[j] > value[j+1]:
                value[j], value[j+1] = value[j+1], value[j]
                key[j], key[j+1] = key[j+1], key[j]
            elif value[j] == value[j+1] and int(key[j][1]) < int(key[j+1][1]):
                value[j], value[j+1] = value[j+1], value[j]
                key[j], key[j+1] = key[j+1], key[j]
​
    for i in range(len(key)-1, -1, -1):
        isi += key[i]+"|"
        banyak_pagar = int(value[i]/50)
        for j in range(banyak_pagar):
            isi += "#"
            if j == banyak_pagar-1:
                isi += " "
        isi += str(value[i])
        if i != 0:
            isi += "\n"
​
    return isi

