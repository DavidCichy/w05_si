def check_if_five(cards_on_hand):
    for i in range(5): 
        if cards_on_hand [i] != cards_on_hand[0]:
            return False
    return True