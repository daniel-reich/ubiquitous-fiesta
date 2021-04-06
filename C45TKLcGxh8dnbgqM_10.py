
def caesar_cipher(s, k):
    result = ''
    k = k%26
    for i in s:
        if 97 <= ord(i) <= 122:
            if ord(i)+k > 122:
                result += chr((ord(i)+k)%122+96)
            else:
                result += chr(ord(i)+k)
        elif 65 <= ord(i) <= 90:
            if ord(i)+k > 90:
                result += chr((ord(i)+k)%90+64)
            else:
                result += chr(ord(i)+k)
        else:
            result += i
    return result

