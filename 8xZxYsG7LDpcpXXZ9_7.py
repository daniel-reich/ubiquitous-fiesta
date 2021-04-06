
import re
​
invalid1 = '.{31}'   ##  greater than 30 characters
invalid2 = '|.{0,4}.$'   ##  or less than 6 greaters 
specchars = "\!\(\)\*\+\[\-\\\\'#$%&,./:;?@\\]^_{|}<=>-"
invalid3   = "|(?!.*[" + specchars + "].*)"   ## no special characters
invalid4 = '|(?!.*[a-z].*)'                   ## no lower case characters
invalid5 = '|(?!.*[A-Z].*)'  ## no upper case alpha
invalid6 = '|(?!.*[0-9].*)'  ## no numbers
invalid = invalid1 + invalid2 + invalid3 +  invalid4 + invalid5 + invalid6
weak1 = '.{6,15}$'  ## length of 6 - 15
weak2 = '(?=[^a-z]*[a-z][^a-z]*[a-z]{0,1}[^a-z]*$)'     ## has 1 or 2 lower case characters (not 3)
weak3 = '(?=[^A-Z]*[A-Z][^A-Z]*[A-Z]{0,1}[^A-Z]*$)'     ## has 1 or 2 Upper case characters (not 3)
weak4 = '(?=[^0-9]*[0-9][^0-9]*[0-9]{0,1}[^0-9]*$)'     ## has 1 or 2 numbers (not 3 )
weak5a = '[' + specchars + ']'
weak5b = '[^' + specchars + ']*'
weak5 = '(?=' + weak5b + weak5a + weak5b + weak5a + '{0,1}' + weak5b + '$)' 
    ## has 1 or 2 special characters (not 3)
weak =  weak1 +  "|" + '(?=.{6,30}$)'  + "(" + weak2 + "|" + weak3 + "|" + weak4 + "|" + weak5  + ')'
 
strong1 = '(?=.{16,30}$)'    ## lenth of 16 - 30
strong2 = '(?=.*[a-z][^a-z]*[a-z][^a-z]*[a-z])'     ## has 3 or more lower case characters
strong3 = '(?=.*[A-Z][^A-Z]*[A-Z][^A-Z]*[A-Z])'     ## has 3 or more Upper case characters
strong4 = '(?=.*[0-9][^0-9]*[0-9][^0-9]*[0-9])'     ## has 3 or more numbers
strong5a = '[' + specchars + ']'
strong5b = '[^' + specchars + ']*'
strong5 = '(?=.*'  + strong5a + strong5b + strong5a + strong5b + strong5a + ')'
    ## has 1 or 2 special characters   
strong =  strong1 +   strong2 + strong3 + strong4 + strong5

