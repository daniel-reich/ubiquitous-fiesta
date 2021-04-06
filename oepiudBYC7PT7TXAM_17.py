
# This is not really a smart way to do, but let's go with this first
# If it works, then I will try to improve it later
​
def parse_roman_numeral(numeral):
​
    letter_to_value = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
    
    total = 0
    
    while True:
        if len(numeral) >= 3:
            # We have a case of ascending numerals, such as: 'IV' (4), 'XL' (40), 'IL' (49), etc.
            if letter_to_value[numeral[1]] > letter_to_value[numeral[0]]:
                total = total + letter_to_value[numeral[1]] - letter_to_value[numeral[0]]
                numeral = numeral[2:]
            # The letters are descending numerals
            else:
                total = total + letter_to_value[numeral[0]]
                numeral = numeral[1:]
        elif len(numeral) == 2:
            # We have a case of ascending numerals, such as: 'IV' (4), 'XL' (40), 'IL' (49), etc.
            if letter_to_value[numeral[1]] > letter_to_value[numeral[0]]:
                total = total + letter_to_value[numeral[1]] - letter_to_value[numeral[0]]
                break
            # The letters are descending numerals
            else:
                total = total + letter_to_value[numeral[1]] + letter_to_value[numeral[0]]
                break
        else:
                total = total + letter_to_value[numeral[0]]
                break
                
    return total

