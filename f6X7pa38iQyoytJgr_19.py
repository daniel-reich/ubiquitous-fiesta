
def increasing_word_weights(st):
   return [sum([ord(j) for j in i if j.isalpha()]) for i in st.split(" ")]==sorted([sum([ord(j) for j in i if j.isalpha()]) for i in st.split(" ")])

