
#edabit
#convert number to base 2
​
def binary(num):
    if num == 0:
        return str(num)
    else:
        binary_string = '' #empty string variable to hold the binary expression.
        while num >= 1: #while loop to test if the given number is greater than 1.
            binary_string += str(num%2) #add the remainder of a division by two calculation to the binary_string variable.
            num = num // 2 #floor divide the number by 2.
    return binary_string[::-1] #reverse the order of the binary_string variable.
​
def main():
    pass
​
if __name__ == "__main__":
    main()

