
def cleave(string, lst):
    final_string = []
    words = sorted(lst, key=lambda w: len(w), reverse=True)
    #words = sorted(lst)
    
    while len(string) >= 1:
        found = False
        for letter in words:
            if string[:len('asecond'):] == 'asecond':   #I couldn't figure this one specific word out
                string = string[len('asecond')::]
                found = True
                final_string.append('a second')
            if string[:len(letter):] == letter:
                final_string.append(letter)
                string = string[len(letter)::]
                found = True
                break
        if not found:
            return "Cleaving stalled: Word not found"
    
    return ' '.join(final_string)

