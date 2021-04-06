
def next_letter(c):
    return 'a' if c == 'z' else chr(ord(c) + 1)
​
def secret_password(message):
    # step 1:
    if len(message) != 9 or not all(['a' <= c <= 'z' for c in message]):
        return "BANG! BANG! BANG!"
    # step 2:
    parts = [message[3*i:3*i+3] for i in range(3)]
    # step 3:
    parts[0] = str(ord(parts[0][0])-96) + parts[0][1] + str(ord(parts[0][2])-96)
    # step 4:
    parts[1] = parts[1][::-1]
    # step 5:
    parts[2] = ''.join([next_letter(c) for c in parts[2]])
    # step 6:
    return parts[1] + parts[2] + parts[0]

