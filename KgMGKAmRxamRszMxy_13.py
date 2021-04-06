
def spartans_cipher(message, n_Slide):
    # go over the message with a while loop
    result = ""
    # calculate how many columns there are
    length_of_message = len(message)
    num_col = length_of_message // n_Slide
    if length_of_message % n_Slide != 0:
        num_col += 1
    # go over it for every slide
    for i in range(num_col):
        letter = i
        for j in range(n_Slide):
            if letter > length_of_message-1:
                result += " "
            else:
                result += message[letter]
            letter += num_col
    # get rid of all spaces at the end
    if len(result) > 0:
        while result[-1] == " ":
            result = result[:-1]
    return result

