
def binary_to_decimal(binary):
    binary = binary[::-1]
    decimal = 0
    for i in range(len(binary)):
        decimal += (binary[i] * (2**i))
    return decimal

