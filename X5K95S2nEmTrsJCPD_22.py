
emotion = {'smile': ':D', 'grin': ':)', 'sad': ':(', 'mad': ':P'}
​
def emotify(txt):
  return "Make me {}".format(emotion[txt.split()[-1]])

