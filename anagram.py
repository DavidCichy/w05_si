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
    '''

    for letter in a:
        if letter not in b:
            return False
    for letter in b:
        if letter not in a:
            return False
    return True