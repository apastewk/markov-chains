from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_file = open(file_path).read()

    return text_file


def make_chains(text_string, text_string2):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """


    chains = {}
    tuple_length = int(raw_input("How long would you like this tuple? ;)"))

    def populate_chain(string_text):
        words = text_string.split()
        keywords = ()
        for i in range(len(words) - 2):
            while tuple_length <= len(words):
                var = 1
                key_words = key_words + words[var]
                var += 1
                if var == tuple_length:
                    break
            # key_words = words[i], words[i + 1]
            value_list = words[i + 2]
            print key_words

            if not chains.get(key_words):
                chains[key_words] = [value_list]
            else:
                chains.get(key_words).append(value_list)
        return chains

    
    populate_chain(text_string)
    populate_chain(text_string2)
    # words = text_string2.split()   

    # for i in range(len(words) - 2):
    #     key_words = words[i], words[i + 1]
    #     value_list = words[i + 2]

    #     if not chains.get(key_words):
    #         chains[key_words] = [value_list]
    #     else:
    #         chains.get(key_words).append(value_list)

    # print chains

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    # got first random tuple. output ('','')
    while True:
        random_key = choice(chains.keys()) 
        new_key = random_key
        # unpack random_key
        thing1, thing2 = random_key
        # added tuple to text string 
        if thing1[0].isupper():
            text = thing1 + " " + thing2
            break
        
    while True:
        # get random_key's corresponding value as a string
        random_value = choice(chains.get(new_key))
        # added new random value to string 
        text = text + " " + str(random_value)
        # created a new tuple to hold the second element of random_key's tuple 
        # and the value of random_key
        new_key = (new_key[1], random_value) 
  
        # if the value of the new key is not in dictionary then break
        if chains.get(new_key) is None:
            lorax, fox = new_key
            last_char = fox[-1]
            if last_char.isalpha() is False:
                break
    return text


# input_path = "gettysburg.txt"
# input_path2 = "green-eggs.txt"
input_path = sys.argv[1]
input_path2 = sys.argv[2]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
input_text2 = open_and_read_file(input_path2)


# Get a Markov chain
chains = make_chains(input_text, input_text2)

# Produce random text
random_text = make_text(chains)

# print random_text
