
import re 
​
def sigilize(desire):
  return remove_vowels(remove_reps_from_end(desire)).upper().replace(" " ,"");
​
def remove_reps_from_end(value):
  removed_letters_from_end  = [value[idx] for idx in range(0 , len(value)) if not value[idx] in value[idx+1:]];
  return "".join(removed_letters_from_end);
​
def remove_vowels(value):
  return re.sub("[aeiouAEIUO]" , "" , value);

