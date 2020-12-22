# If you're having a hard time understanding, it maybe helpful to read these
# instructions first. If you don't know a certain built-in function, method
# or something else google it like this. "pyton itemgetter()". I generally refer to
# w3schools.com and stackoverflow.com. If the first answer of stackoverflow is 
# too complicated, take a look at the second one. They are generally easier to understand.

# First analyze open_file() starting at line (sal.) 83. Then read through 95-100.
# Analyze build_map(in_file, word_map) sal. 83. At line 49 notice line 55, stop and analyze 
# add_word(word_map, word) sal. 17. Get back to line 51. Notice line 101 and
# Analyze display_map(word_map).



import string
from operator import itemgetter

def add_word( word_map, word ):

    # For each word in the text (passed to this function from build_map())
    # if it wasn't added before to word_map, initialize a key for that word
    # and make its value 0. 
    if word not in word_map:
        word_map[ word ] = 0

    # If the key has been newly initialized, make its value 1. In the case
    # that the key is not a new one, if structure will not be processed and 
    # its value will be increased by 1. 
    # Basically, add each word into a dict and count their occurences.
    word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:

        # For each line, split the string "line" into a list where each 
        # word of the current line is a an item of the list.
        word_list = line.split()

        for word in word_list:

            # string.punctuation is a pre-initialized string that returns 
            # all sets of punctuation. Try print(string.punctutation) 
            # import the string module beforehand.

            # Strip any punctuation from the current word of the current line.
            # word_map is an empty dict declared on line X and passed to 
            # this function at line X. For each word of the current line call
            # this function w/ arguments word_map, word.
            word = word.strip(string.punctuation)
            # At this point every word has been passed to add_word(word_map, word)
            # Now we have a dict, word_map, containing all words as keys and number
            # of their occurences as their values.
            
            add_word( word_map, word )
        

def display_map( word_map ):

    word_list = list()

    # Create and empty list, word_list, and for each key and value in word_map
    # append them together as an tuple to this list.
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # For each tuple in the list sort according to their frequencies (because 
    # itemgetter(1) refers to the second item, freq) in ascending order. If two 
    # items have the same number of occurences, preserve original order.
    # See, sorting stability.
    # Still confused ? 
    # https://docs.python.org/3/howto/sorting.html
    # https://www.w3schools.com/python/ref_func_sorted.asp
    # Scroll to bottom and play with the code.
    freq_list = sorted( word_list, key=itemgetter(1) )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():

    try:
        in_file = open( "document1.txt", "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()



# Sorting

a = [(1,5,9), (2,4,8), (3,6,7)]
for i in range(3):
	print(sorted(a, key=itemgetter(i)))
b = [(1,2), (0,2)]
print(sorted(b, key=itemgetter(1)))