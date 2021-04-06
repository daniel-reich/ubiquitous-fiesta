
import string 
def markdown(character):
    def apply(txt, markdown_word):
        def matches(word):
            return markdown_word.lower() == word.translate(str.maketrans('','',string.punctuation)).lower()
​
        words = [character + word + character if matches(word) else word for word in txt.split() ]
        for word in words:
            word.translate(str.maketrans('', '', string.punctuation))
        return " ".join(words)
    return apply

