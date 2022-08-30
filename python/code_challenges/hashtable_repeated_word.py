from data_structures.hashtable import Hashtable
import re

def first_repeated_word(words):
    """
    Find the first repeated word in the text

    :params words: string, original text
    :return: string
    """
    hashtable = Hashtable()
    words_list = re.split(r"[\W+]?\s+", words)
    for word in words_list:
        lower_word = word.lower()
        if hashtable.get(lower_word):
            return lower_word
        else:
            hashtable.set(lower_word, word)
    return None


#######################
#### Stretch Goals ####
#######################

def count_words(words):
    """
    Return a count of each of the words in the provided string

    :params words: string, original text
    :return: int, the count of each of the words
    """
    if words == "":
        return 0

    count = 0
    hashtable = Hashtable()
    words_list = re.split(r"[\W+]?\s+", words)
    for word in words_list:
        if word != "":
            count +=1
    return count

def get_most_frequent(words):
    """
    Return a list of the words most frequently used in the provided string

    :params words: string, original text
    :return : list, most frequent words in text
    """

    if words == "":
        return []
    hashtable = Hashtable()
    words_list = re.split(r"[\W+]?\s+", words)

    dic={}
    for word in words_list:
        lower_word = word.lower()
        if not dic.get(lower_word):
            dic[lower_word] = [word]
        else:
            dic.get(lower_word).append(word)
    print(dic)
    temp = []
    for key, value in dic.items():
        if len(value) > len(temp):
            temp = value

    return temp
