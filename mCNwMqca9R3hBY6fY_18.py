
sad_faces = [":(", "8(", "x(", ";("]
happy_faces = [":)", "8)", "x)", ";)"]
​
def make_happy(sentence):
    for i in range(0,4):
        sentence = sentence.replace(sad_faces[i], happy_faces[i])
    return sentence

