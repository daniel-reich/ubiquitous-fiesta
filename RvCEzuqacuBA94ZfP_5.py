
import re
def generate_hashtag(txt):
    txt = ''.join(list(map(lambda x:x.capitalize(),re.sub(r'\s+'," ",txt).split(" "))))
    return '#'+txt if len(txt)!=0 and len(txt)<140 else False

