
def bit_rotate(n, m, d):
    binary = bin(n)[2::]
    new_binary = ['0'] * len(binary)
    if not(d): # to the left
        temp = []
        for i in binary:
            temp = [ i ] + temp
        binary = temp
    for i in range(len(binary)):
        if binary[i] == "1":
            place = (i + m) % len(binary)
            new_binary[place] = "1"
    
    if not(d):
        new_binary.reverse()
​
    binary = int("".join(new_binary))
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
​
    return decimal

