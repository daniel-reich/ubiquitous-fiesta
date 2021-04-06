
def secret(txt):
    tag, *class_name = txt.split(".")
    return "<{} class='{}'></{}>".format(tag, " ".join(class_name), tag)

