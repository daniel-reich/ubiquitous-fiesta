
import re
def wurst_is_better(txt):
    sausages = r'.(ielbasa|horizo|oronga|alami|ausage|ndouille|aem|erguez|urka|norker|epperoni)(s)*'
    wursttxt = re.sub(sausages, 'Wurst', txt)
    return wursttxt

