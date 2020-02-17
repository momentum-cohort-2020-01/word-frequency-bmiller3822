STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def print_word_freq(file):
    
    with open('seneca_falls.txt', 'r') as file:
        data = file.read()

    no_punctuation = ""
    for character in data:
        if character not in punctuations:
            no_punctuation = no_punctuation + character

    my_string = no_punctuation.lower()

    my_string = [word for word in my_string.split() if word not in STOP_WORDS]

    def word_count(my_string):
        counts = {}
        
        for word in my_string:
            if word in counts:
                counts[word] += 1
            else: 
                counts[word] = 1
            
        return counts

    new_string = word_count(my_string)

    sorted_string = sorted(new_string.items(), key = 
            lambda kv: (kv[1], kv[0]))

    print (sorted_string)



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)



# ========================Notes and other nonsense=====================================

    # for key, value in sorted_string.items():
    #     print (key, ' : ', value)

# print(sorted(key_value.items(), key = 
#              lambda kv:(kv[1], kv[0])))
#methods on dictionaries


# This didn't work to have them line by line unfortunately. 
#  new_string = word_count(my_string)

#     for elem in new_string:
#         print (new_string)

# This didn't work either:
# def format(counts):
#         for word, count in counts.items():
#             print (f'{name}: {score}')

#     format(counts)



#new_string = (word_count(my_string))

    # for key, value in new_string.items():
    #     print (key, ' : ', value)



     #, "\n"

    # print ('\n'.join(f"{word}: {counts}"))
    # word_count(my_string)

    #     return counts

    # print ( word_count(my_string))
    

    #Try .items()


    # print ( word_count(my_string))

# sorted_string = [item for item in sorted_string.split() if item not in STOP_WORDS]




    #This does everything but have them in a column vs just a wall of text.  I feel like I'm about to break it again so here we are:
    # def print_word_freq(file):
    
    # with open('seneca_falls.txt', 'r') as file:
    #     data = file.read()

    # no_punctuation = ""
    # for character in data:
    #     if character not in punctuations:
    #         no_punctuation = no_punctuation + character

    # my_string = no_punctuation.lower()

    # my_string = [word for word in my_string.split() if word not in STOP_WORDS]

    # def word_count(my_string):
    #     counts = {}
        
    #     for word in my_string:
    #         if word in counts:
    #             counts[word] += 1
    #         else: 
    #             counts[word] = 1
            
    #     return counts

    # new_string = word_count(my_string)

    # sorted_string = sorted(new_string.items(), key = 
    #         lambda kv: (kv[1], kv[0]))

    # print (sorted_string)


    #Failed attempt at fully sorting, but I'm happy with what I've gotten today. 
    # def print_word_freq(file):
    
    # with open('seneca_falls.txt', 'r') as file:
    #     data = file.read()

    # no_punctuation = ""
    # for character in data:
    #     if character not in punctuations:
    #         no_punctuation = no_punctuation + character

    # my_string = no_punctuation.lower()

    # my_string = [word for word in my_string.split() if word not in STOP_WORDS]

    # def word_count(my_string):
    #     counts = {}
        
    #     for word in my_string:
    #         if word in counts:
    #             counts[word] += 1
    #         else: 
    #             counts[word] = 1
            
    #     return counts

    # new_string = word_count(my_string)

    # sorted_string = sorted(new_string.items(), key = 
    #         lambda kv: (kv[1], kv[0]))

    # def fully_sorted(sorted_string):
    #     counts_two = {}
        
    #     for item in sorted_string:
    #         if item in counts_two:
    #             counts_two[item] = counts_two[item]
                
    #     return counts_two 

    # fully_sorted_string = fully_sorted(sorted_string)

    # for key, value in fully_sorted_string.items():
    #      print (key, ' : ', value)