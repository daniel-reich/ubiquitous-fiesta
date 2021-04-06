
import re
​
def small_favor(sentence):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    pattern1 = re.compile(r"\d{2}[/.]\d{2}[/.](\d{2})")
    pattern2 = re.compile(r"(\w+), \d{2}\. (\d{2})\.")
​
    def replace1(match):
        old = match.group(1)
        new = "20" + old if int(old) < 25 else "19" + old
        match = match.group(0)
        return match[:-len(old)] + new
​
    def replace2(match):
        if match.group(1) not in months:
            return match.group(0)
        old = match.group(2)
        new = "20" + old if int(old) < 25 else "19" + old
        match = match.group(0)
        return match[:-len(old)-1] + new + "."
​
    sentence = re.sub(pattern1, replace1, sentence)
    sentence = re.sub(pattern2, replace2, sentence)
​
    return sentence

