
def make_dictonary_of_hand(cards_on_hand):
    cards_dict = {}
    for item in cards_on_hand:
        if item in cards_dict:
            cards_dict[item] += 1
        else:
            cards_dict[item] = 1
    return cards_dict

def check_if_five(cards_on_hand):
    for i in range(5): 
        if cards_on_hand [i] != cards_on_hand[0]:
            return False
    return True
