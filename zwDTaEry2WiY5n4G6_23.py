
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
def digital_vowel_ban(num,ban):
    number=''
    for nums in list(str(num)):
        word=words[int(nums)]
        if ban in str(word):
            continue
        else:
            number=number+str(nums)
    if number =='':
        number = "Banned Number"
    else: number=int(number)
    return number

