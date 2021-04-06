
def words_to_sentence(words):
  cleaned_words  = words and [e for e in words if e != ""];
  if (cleaned_words is None or len(cleaned_words) == 0) :
    return "";
  if (len(cleaned_words) == 1):
    return cleaned_words[0];
    
  left = cleaned_words[0:-1];
  right = cleaned_words[-1];
  return "{0} and {1}".format(", ".join(left) , right);

