from cs50 import get_string

letters, words, sentences = 0, 0, 0 #make a list of the variables we need to use
s = get_string ("Text: ").strip() #strip gets rid of any unwanted spaces at the beginning and end of a string

for i in range(len(s)): #we use in range in python. move the index along the length of the string (s)
    if s[i].isalpha(): #we need isalpha again to determine case. string[index](meaning letter).isalpha (we need . to use a function and . basically means inside here)
        letters += 1 #with += right is added to left. or letter count here.
    if (i == 0 and s[i] != ' ') or (i != len(s) - 1 and s[i] == ' ' and s[i + 1] != ' '): #repeat formula. these bounderaries identify spaces.
        words += 1 #word count + 1
    if (s[i] == '.' or s[i] == '?' or s[i] == '!'): #identify punctuation.
        sentences += 1

L = letters / words * 100 #L = our letter count / word count (* 100 as per the coleman-liau)
S = sentences / words * 100 #S = our sentence count / word count
grade = round(0.0588 * L - 0.296 * S - 15.8) #to get a grade average number we must round the decimals
if grade < 1:
    print ("Before Grade 1")
elif grade >= 16:
    print ("Grade 16+")
else:
    print (f"Grade:{grade}")