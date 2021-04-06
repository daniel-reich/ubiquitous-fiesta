
def cipher(input_arg):
    output = [ord(input_arg[0])]
    for i in range(len(input_arg) - 1):
        output.append(ord(input_arg[i + 1]) - ord(input_arg[i]))
    return output
​
​
def decipher(input_arg):
    result = ''
    current_sum = 0
    for i in range(len(input_arg)):
        current_sum += input_arg[i]
        result += chr(current_sum)
    return result
​
​
def dif_ciph(input):
    if type(input) == list:
        return decipher(input)
    return cipher(input)

