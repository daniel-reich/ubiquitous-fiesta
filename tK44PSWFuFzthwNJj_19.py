
import string
​
​
def club_entry(word):
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    numlst=[]
    for i in range(1,27):
        numlst.append(i)
    combined_dict=dict(zip(alphabet_list,numlst))
    for i in word:
        if word.count(i)==2 and word.find(i+i)!=-1:
            return combined_dict[i]*4

