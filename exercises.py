'''
Here are some exercises. Try to write a function header and doctests first, and only then implement the function.

1/ Check what is the most frequent number in an array. If there are multiple such numbers, return the largest one. For instance, most_frequent([3, 3, 3, 2, 2, 2, 4, 4]) should return 3.
2/ Calculate a cyclic rotation of a string; i.e. move the last N elements from the end to the beginning. For example, cyclic_rotation('abcde', 2) should return 'deabc'.
3/ Write a poker_hand function that will score a poker hand. The function will take an array 5 numbers and return a string based on what is inside. It should recognize the following patterns:

Name 	Description 	Example
five 	five of a kind 	[1, 1, 1, 1, 1]
four 	four of a kind 	[2, 2, 2, 2, 3]
three 	three of a kind 	[1, 1, 1, 2, 3]
twopairs 	two pairs 	[2, 2, 3, 3, 4]
pair 	a single pair 	[1, 2, 2, 3, 4]
fullhouse 	a pair and a three 	[1, 1, 2, 2, 2]
nothing 	none of the above 	[1, 2, 3, 4, 6]
'''


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