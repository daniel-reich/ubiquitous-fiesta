
def mirror_cipher(message, key="".join([chr(i) for i in range(ord('a'), ord('z') + 1)])):
    message, key, message_list = message.lower(), key.lower(), list(message.lower())
    for i, letter in enumerate(message):
        if letter in key:
            replacement_character = key[(len(key) - 1) - (key.find(letter))]
            message_list[i] = replacement_character
    return "".join(message_list)

