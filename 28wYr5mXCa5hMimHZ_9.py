
import re
def valid_name(name):
    valid_formats = ['I. Word', 'I. I. Word',
                  'Word I. Word', 'Word Word Word']
    def name_format(name):
        def word_format(word):
            if re.search('^[A-Z].{2,}$', word) and not '.' in word:
                return 'Word'
            elif re.search('^[A-Z]\.$', word):
                return 'I.'
            return 'Ni una cosa ni la otra'
        return ' '.join([word_format(word) for word in name.split()])
    return name_format(name) in valid_formats

