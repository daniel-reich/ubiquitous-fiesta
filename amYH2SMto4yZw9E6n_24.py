
import re
def validate(s):
    is_valid = False
    seps = ('', ' ', '.', '-', '/', '0')
    for sep in seps:
        sep = re.escape(sep)
        if sep == '\\-':
            pattern = '(\\+?{1}{0})?{2}{0}{2}{0}{3}'.format(sep,'\d{1}','\d{3}','\d{4}')
        elif sep == '0':
            pattern = '({1} )?{4}{2}{5} {2}{0}{3}'.format(re.escape('-'),'\d{1}','\d{3}','\d{4}',re.escape('('),re.escape(')'))
        else:
            pattern = '({1}{0})?{2}{0}{2}{0}{3}'.format(sep,'\d{1}','\d{3}','\d{4}')
        is_valid = is_valid or bool(re.fullmatch(pattern, s))
    return is_valid

