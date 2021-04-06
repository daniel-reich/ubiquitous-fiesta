
import string
def average_word_length(txt):
    exclude = set(string.punctuation)    
    r = [len(i) for i in ''.join([i for i in txt if i not in exclude]).split()]    
    return round(sum(r)/len(r),2)

