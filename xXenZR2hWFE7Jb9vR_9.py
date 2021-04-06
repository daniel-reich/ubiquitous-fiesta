
def is_isomorphic(s, t):
    s.lower();t.lower();
    alphabet={};values=[];
    for i in range(len(s)):
        # if the character in string s does not point to anything yet, and the character in string t is not pointed by anything,
        #create a mapping from s[i] to t[i] 
        if(s[i] not in alphabet):
            if(t[i] not in values):
                alphabet.update({s[i]:t[i]});
                values.append(t[i]);
            else:
                return False;            # if the character in string s point to a character in t that has been pointed, return false
        elif(alphabet[s[i]] != t[i]):
            return False;                # if there is already a mapping from s[i], but not to t[i],this means that two strings are not isomorphic
        
    #print(alphabet)
    return True;

