
def add_letters(a):
    if not a:
        return 'z'
    letters = 'z a b c d e f g h i j k l m n o p q r s t u v w x y '.strip().split()
    nums = range(0,26)
    letters_num = dict(zip(letters,nums))
    list_sum = 0
    for l in a:
        list_sum += letters_num[l]
    num_converted = list_sum % 26
    for k,v in letters_num.items():
        if v == num_converted:
            return k

