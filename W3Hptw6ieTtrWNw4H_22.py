
def bifid(text):
    coords = [str(i) + str(j) for i in range(1, 6) for j in range(1, 6)]
    encrypt = dict(zip('abcdefghiklmnopqrstuvwxyz', coords))
    decrypt = dict(zip(coords, 'abcdefghiklmnopqrstuvwxyz'))
​
    if text[0].isupper():
        text = ''.join(i for i in text.lower() if i.isalpha())
        nums = text.replace('j', 'i').translate(str.maketrans(encrypt))
        new = ''.join(nums[::2] + nums[1::2])
        return ''.join(decrypt[new[i:i+2]] for i in range(0, len(new), 2))
    else:
        nums = text.replace('j', 'i').translate(str.maketrans(encrypt))
        new = (a + b for a, b in zip(nums[:len(nums)//2], nums[len(nums)//2:]))
        return ''.join(decrypt[i] for i in new)

