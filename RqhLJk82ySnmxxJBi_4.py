
answers = {9: "Polymorphic", 4: "Quadrimorphic", 2: "Dimorphic",
           1: "Enamorphic"}
​
def power_morphic(num):
    mod = 10**len(str(num))
    powers = [p for p in range(2, 11) if num**p % mod == num]
    n = len(powers)
    return answers.get(n, "Amorphic")

