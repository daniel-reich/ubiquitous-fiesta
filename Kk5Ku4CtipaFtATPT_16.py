
def coconut_translator(s):
    letter = "coconuts"
    bins = ' '.join((8-len(format(ord(item),'b'))) * '0'+ format(ord(item),'b') 
                    if len(format(ord(item),'b')) != 8 else format(ord(item),'b') for item in s).split()
    result =''.join([letter[i] if nums[i] == '0' else letter[i].upper() for nums in bins for i in range(8) ])
    return ' '.join(result[i:i+8] for i in range(0,len(result),8))

