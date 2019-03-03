import poker_hand_logic


def most_frequent_number_in_array(array):
    '''
    Check what is the most frequent number in an array.

    >>> most_frequent_number_in_array([3, 3, 3, 2, 2, 2, 4, 4])
    3

    >>> most_frequent_number_in_array([3, 3, 3, 5, 5, 5, 7, 7, 0, 2, 2, 2])
    5
    '''
    array.sort()
    dict_of_array = {}
    highest_number_frequency = 0

    for number in array:
        if number in dict_of_array.keys():
            dict_of_array[number] +=1
        else:
            dict_of_array[number] = 1

    for number in dict_of_array:
        if dict_of_array[number] >= highest_number_frequency:
            highest_number_frequency = dict_of_array[number]
            most_frequent_number = number
    return most_frequent_number


def cyclic_rotation(input_string, rotation):
    '''
    Calculate a cyclic rotation of a string; 
    i.e. move the last N elements from the end to the beginning. 
    For example, cyclic_rotation('abcde', 2) should return 'deabc'.
    >>> cyclic_rotation('abcde', 2)
    'deabc'
    >>> cyclic_rotation('abvba', 5)
    'abvba'
    >>> cyclic_rotation('abcde', -2)
    'cdeab'
    '''
    string_list = list(input_string)
    string_len = len(input_string)
    string_last_index = string_len - 1
    new_string_list = list(input_string)
    string_character_id = 0
    new_string = ""

    for character in string_list:
        new_string_character_id = string_character_id + rotation
        
        if new_string_character_id > string_last_index:
            new_string_character_id -= string_len

        new_string_list[new_string_character_id] = str(character)
        string_character_id += 1

    new_string = ''.join(new_string_list)

    return new_string


def poker_hand(cards_on_hand):
    '''
    Write a poker_hand function that will score a poker hand. 
    The function will take an array 5 numbers and 
    return a string based on what is inside. 
    It should recognize the following patterns:
    five 	five of a kind 	[1, 1, 1, 1, 1]
    four 	four of a kind 	[2, 2, 2, 2, 3]
    three 	three of a kind 	[1, 1, 1, 2, 3]
    twopairs 	two pairs 	[2, 2, 3, 3, 4]
    pair 	a single pair 	[1, 2, 2, 3, 4]
    fullhouse 	a pair and a three 	[1, 1, 2, 2, 2]
    nothing 	none of the above 	[1, 2, 3, 4, 6]
    
    >>> poker_hand([1, 1, 1, 1, 1])
    'five'
    >>> poker_hand([2, 2, 2, 2, 3])
    'four'
    >>> poker_hand([2, 2, 3, 3, 4])
    'twopairs'
    >>> poker_hand([2, 2, 2, 3, 4])
    'three'
    >>> poker_hand([1, 2, 2, 3, 4])
    'pair'
    >>> poker_hand([1, 1, 2, 2, 2])
    'fullhouse'
    >>> poker_hand([1, 2, 3, 4, 6])
    'nothing'
    '''
    cards_dict = poker_hand_logic.make_dictonary_of_hand(cards_on_hand)
    
    if poker_hand_logic.check_if_five(cards_dict):
        return 'five'

    elif poker_hand_logic.check_if_four(cards_dict):
        return 'four'
    
    elif poker_hand_logic.check_if_fullhouse(cards_dict):
        return 'fullhouse'
    
    elif poker_hand_logic.check_if_three(cards_dict):
        return 'three'
    
    elif poker_hand_logic.check_if_twopairs(cards_dict):
        return 'twopairs'
    
    elif poker_hand_logic.check_if_pair(cards_dict):
        return 'pair'
    
    else:
        return 'nothing'