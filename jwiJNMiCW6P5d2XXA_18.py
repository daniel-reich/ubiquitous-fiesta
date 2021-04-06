
def does_rhyme(s1,s2):
    s1=s1.split()[-1]
    s2=s2.split()[-1]
    vowels='aeiou'
    s1_ch=[x.lower() for x in s1 if x.isalnum() and x.lower() in vowels]
    s2_ch=[x.lower() for x in s2 if x.isalnum() and x.lower() in vowels]
    if s1_ch==s2_ch:
        return True
    else:
        return False

