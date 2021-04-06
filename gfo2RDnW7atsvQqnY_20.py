
def count_smileys(lst):
    return lst.count('(:') + lst.count(':)') + lst.count(':-D') + lst.count(';D') + lst.count(':-)') + lst.count(';~)') + lst.count(';-D') + lst.count(':D') + lst.count(';~D')

