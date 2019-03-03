
def make_dictonary_of_hand(cards_on_hand):
    cards_dict = {}
    for item in cards_on_hand:
        if item in cards_dict:
            cards_dict[item] += 1
        else:
            cards_dict[item] = 1
    return cards_dict

def check_if_five(cards_dict):
    for key in cards_dict:
        if cards_dict[key] == 5:
                return True
    return False

def check_if_four(cards_dict):
    for key in cards_dict:
        if cards_dict[key] == 4:
                return True
    return False