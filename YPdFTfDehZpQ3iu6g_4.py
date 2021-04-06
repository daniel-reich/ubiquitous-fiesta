
def roman_numerals(arg):
    convertRomNum = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, '0': 0}
    convertNumRom = ({'borrow': 'X', 'base': 'V', 'add': 'I'},
                     {'borrow': 'C', 'base': 'L', 'add': 'X'},
                     {'borrow': 'M', 'base': 'D', 'add': 'C'})
​
    if type(arg) == str:
        rom = arg
        rom += '0'
        numList = []
        for i in range(len(rom) - 1):
            if convertRomNum[rom[i]] < convertRomNum[rom[i + 1]]:
                numList.append(convertRomNum[rom[i]] * - 1)
            else:
                numList.append(convertRomNum[rom[i]])
                
        return sum(numList)
​
    if type(arg) == int:
        num = str(arg)[::-1]
        romString = ''
        for i in range(3):
            if i == len(num):
                break
            if num[i] == '9':
                romString += convertNumRom[i]['borrow'] + convertNumRom[i]['add']
            elif 9 > int(num[i]) > 4:
                for j in range(int(num[i]) - 5):
                    romString += convertNumRom[i]['add']
                romString += convertNumRom[i]['base']
            elif num[i] == '4':
                romString += convertNumRom[i]['base'] + convertNumRom[i]['add']
            else:
                for j in range(int(num[i])):
                    romString += convertNumRom[i]['add'] 
        
        return int(num[3:]) * 'M' + romString[::-1] if len(num) > 3 else romString[::-1]

