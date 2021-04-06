
def generate_palindromes(number):
    palindromes = []
    for i in range(10,number+1,1):
        reverse = list(str(i))
        reverse.reverse()
        if i == int("".join(reverse)):
            palindromes.append(i)
    palindromes.sort()
    return palindromes[len(palindromes)-15:len(palindromes):1]

