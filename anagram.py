def is_anagram(a, b):
    '''
    Checks if the two words are anagrams, that is, if letters in one word can
    be rearranged to give the other.

    >>> is_anagram('listen', 'silent')
    True
    >>> is_anagram('aabcd', 'dabac')
    True
    >>> is_anagram('cat', 'dog')
    False
    >>> is_anagram('abc', 'defgh')
    False
    >>> is_anagram('aab', 'abb')
    False
    '''
    a_in_list = list(a)
    b_in_list = list(b)
    a_in_list.sort()
    b_in_list.sort()
    if  a_in_list == b_in_list:
        return True
    return False