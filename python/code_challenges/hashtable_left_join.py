from data_structures.hashtable import Hashtable


def left_join(synonyms, antonyms):
    """
    Implement a simplified LEFT JOIN for 2 hashmaps

    :params synonyms: hashmap
    :params antonyms: hashmap
    :return : list
    """
    result = []
    for key, value in synonyms.items():
        if antonyms.get(key):
            result.append([key, value, antonyms.get(key)])
        else:
            result.append([key, value, "NONE"])
    return result

##################
## Stretch goal ##
##################

def right_join(synonyms, antonyms):
    return left_join(antonyms, synonyms)
