# Take the data in the .txt file and use the following: 
# no_specials_string = re.sub('[!#?,.:";]', '', data)
# print(no_specials_string)
#Second option from Ryan: https://www.programiz.com/python-programming/examples/remove-punctuation

# Take the data in the .txt file and use the following to make it lowercase:
# string.lower()
# (Might need to look at Jupyter on how to concat strings if necessary)

#=======Made it here so far ========

# Loop through all of the words in the string and use:
# Remove stop words
# [word for word in tokenized_words if word not in stop_words]
# May need to assign this to a variable perhaps?
# https://chrisalbon.com/machine_learning/preprocessing_text/remove_stop_words/

# #  Run through the text word for word and count each one:


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

with open('seneca_falls.txt', 'r') as f:
    data = f.read()

no_punctuation = ""
for character in data:
    if character not in punctuations:
        no_punctuation = no_punctuation + character

my_string = no_punctuation.lower()

# print (my_string) //This worked

# print (my_string.split()) //This worked

my_string = [word for word in my_string.split() if word not in STOP_WORDS]

print (my_string) #This worked

#WOOP WOOP now I'm down here!



# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     return counts

# print( word_count('the quick brown fox jumps over the lazy dog.'))

# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php

# When your program is complete, you should be able to run python3 word_frequency.py seneca_falls.txt and get a printed report like this:






