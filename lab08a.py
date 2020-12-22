import string
from operator import itemgetter

def add_word( word_map, word ):
    """
    Add word, if it hasn't been added before and is not an empty string, and 
    count its occurences
    """
    
    if word.isalpha() == True:
        if word not in word_map:
            word_map[ word ] = 0

        word_map[ word ] += 1


def build_map( in_file, word_map ):    
    """
    Isolate each string in the text and send them as a parameter to add_word() function.
    """

    for line in in_file:

        # For each line, split the string "line" into a list.    
        word_list = line.split()

        for word in word_list:

            # Strip any punctuation from the current word and lowercase it.
            word = word.strip(string.punctuation).lower()
            add_word( word_map, word )

def display_map( word_map ):
    """
    Construct a list from the dict and first sort alphabetically and then by frequencies. 
    Print the formatted result.
    """

    word_list = list()

    # For each key and value in word_map append them together as a tuple to word_list.
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # For each tuple in the list sort according to their frequencies in ascending order. 
    # If two items have the same number of occurences, preserve original order.
    freq_list = sorted( sorted(word_list), key=itemgetter(1), reverse=True)


    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )

def open_file():
    """
    Try to get the name of the file from the user. 
    Open the file and return as readable.
    """

    try:
        file_name = input("Enter the name of the document: ")
        in_file = open( file_name, "r" )
        
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


