
AUTOMORPHISM = {
    0: "Amorphic",
    1: 'Enamorphic',
    2: "Dimorphic",
    4: "Quadrimorphic",
    9: "Polymorphic"
}
​
def power_morphic(num):
    
    string_num = str(num)
    count = 0
​
    for i in range(2,11):
        if str(num**i)[-1 * len(str(num)):] == str(num):
            count += 1
​
    return AUTOMORPHISM[count]

