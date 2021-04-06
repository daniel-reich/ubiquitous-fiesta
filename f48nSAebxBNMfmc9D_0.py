
import re; scrambled = lambda w, m: [i for i in w if re.match("^"+m.replace('*', r'\w')+"$", i)]

