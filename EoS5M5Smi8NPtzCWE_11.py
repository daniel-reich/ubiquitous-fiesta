
def secret(text):
    text = text.split('*')
    return "<{}></{}>".format(text[0],text[0])*(int(text[1]))

