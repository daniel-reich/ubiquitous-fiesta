
def generate_hashtag(astring):
    if astring.strip() == '':
        return False
    else:
        updated_string = astring.strip()
        emptystring = ''
        split_updated_string = updated_string.split(' ')
        for eachword in split_updated_string:
            emptystring += eachword.capitalize()
        final_string = "#" + emptystring
        return final_string if len(final_string) < 140 else False

