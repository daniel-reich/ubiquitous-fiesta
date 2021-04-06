
pronomi={
    'first': {'sing': 'Io', 'pl': 'Noi'},
    'sec': {'sing': 'Tu', 'pl': 'Voi'},
    'third': {'sing': 'Lui/Lei', 'pl': 'Loro'}}
verbi_spec = {
    'first': {'sing': ['o', 'o', 'o'], 'pl': ['ia', 'ia', 'ia']},
    'sec': {'sing': ['i', 'i', 'i'], 'pl': ['a', 'e', 'i']},
    'third': {'sing': ['a', 'e', 'e'], 'pl': ['a', 'o', 'o']}}
verbi_com={
    'first': {'sing': '', 'pl': 'mo'},
    'sec': {'sing': '', 'pl': 'te'},
    'third': {'sing': '', 'pl': 'no'}}
def inflect(verb, person, number):
    word = verb[-3]
    if word=="a":
        x = 0
    if word=="e":
        x = 1
    if word=="i":
        x = 2
    return pronomi[person][number]+' '+ verb [:-3] + verbi_spec[person][number][x]+ verbi_com[person][number]

