
from string import ascii_uppercase
def coconut_translator(string):
    cn = "coconuts"
    coconut = ""
    for ch in string:
        bin_str = str(bin(ord(ch)))[2:]   #convert character to binary string and remove '0b'.
        bin_str = '0'*(8-len(bin_str)) + bin_str  #pad front of binary string with 0's
        for i in range(len(bin_str)):
            if bin_str[i] == '1':
                cn = cn[:i] + cn[i].upper() + cn[i+1:] 
        coconut += cn + ' '
        cn = "coconuts" 
    return coconut.rstrip()

