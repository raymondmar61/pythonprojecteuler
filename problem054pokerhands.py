#YouTube Project Euler Problem 54： Poker Hands [mDBA3ZHcTWo]
#The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space):the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

#Dictionary suits and values.  Index starts at 0.  Ascending order 0 is lowest.
suitsdictionary = {"S":3, "H":2, "C":1, "D":0}
valuesdictionary = {"A":12, "K":11, "Q":10, "J":9, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, "2":0}

def sort_hand(hand):
    new_handarray = [""] * 52 #new array with 52 empty strings
    for card in hand:
        value, suit = [*card] #get value and suit of the card
        index = valuesdictionary[value] + (13 * suitsdictionary[suit])
        new_handarray[index] = card #put card in proper index of the array
    return [c for c in new_handarray if c != ""] #remove empty strings and return hand
def is_flush(hand):
    suit = hand[0][1] #get the suit from the first card in the hand
    for card in hand: #for each card in the hand, check to see if any cards of the hand doesn't contain the suit from the first card
        if not suit in card: #
            return False
    #print("found a flush",hand) #print found a flush ['2H', '4H', '6H', '8H', 'KH']
    return True
def is_straight(hand):
    valsisstraight = [valuesdictionary[c[0]] for c in hand]
    valsisstraight.sort()
    first_val = valsisstraight[0]
    next_val = first_val + 1
    for i in range(1, 5):
        if valsisstraight[i] != next_val:
            return False
        next_val += 1
    #print("found a straight",hand) #print found a straight ['5C', '2H', '3H', '4H', '6H']
    return True
def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)

def is_royal_flush(hand):
    return is_straight_flush(hand) and hand[0][0] == "T"

#Four of a kind, three of a kind
def find_num_values(hand):
    num_vals = {}
    for cardeach in hand:
        val = cardeach[0]
        num_vals[val] = num_vals.get(val, 0) + 1
    return num_vals

def is_pair_of_pairs(num_vals):
    #look for two 2s
    count = 0
    for val in num_vals.values():
        if val == 2:
            count += 1
    if count == 2:
        return True
    return False

def find_winner_by_highest_value(num_vals1, num_vals2):
    scores1 = [valuesdictionary[val] for val in num_vals1]
    scores2 = [valuesdictionary[val] for val in num_vals2]
    scores1.sort()
    scores2.sort()
    while scores1 and scores2:
        scored1 = scores1.pop()
        scored2 = scores2.pop()
        if scored1 > scored2:
            return 1
        if scored2 > scored1:
            return 2
    return 1

#Assign a score based on the hand:  royal flush 10, straight flush 9, four of a kind 8 to high card 1
def evaluate_winner(hand1, hand2):
    #print(f"evaluate_winner function hands {hand1} and {hand2}") #print evaluate_winner function hands ['8C', 'KC', '9H', '4S', 'TS'] and ['5D', '7D', 'AC', '2S', '3S']
    if is_royal_flush(hand1):
        return hand1, "royal flush"
    if is_royal_flush(hand2):
        return hand2, "royal flush"
    num_vals1 = find_num_values(hand1)
    num_vals2 = find_num_values(hand2)
    winner_by_highest_value = find_winner_by_highest_value(num_vals1, num_vals2)

    if is_straight_flush(hand1):
        if is_straight_flush(hand2):
            print("Comparing straight flush.  Winner by highest value is", winner_by_highest_value)
            if winner_by_highest_value == 1:
                return hand1, "straight flush"
            return hand2, "straight flush"
        return hand1, "straight flush"
    if is_straight_flush(hand2):
        return hand2, "straight flush"
    if 4 in num_vals1.values(): #four of a kind
        if 4 in num_vals2.values():
            print("Comparing four of a kind.  Winner by highest value is", winner_by_highest_value)
            if winner_by_highest_value == 1:
                return hand1, "four of a kind"
            return hand2, "four of a kind"
        return hand1, "four of a kind"
    if 4 in num_vals2.values():
        return hand2, "found of a kind"
    if 3 in num_vals1.values() and 2 in num_vals1.values(): #full house
        if 3 in num_vals2.values() and 2 in num_vals2.values():
            print("Comparing full house.  Winner by highest value is", winner_by_highest_value)
            if winner_by_highest_value == 1:
                return hand1, "full house"
            return hand2, "full house"
        return hand1, "full house"
    if 3 in num_vals1.values() and 2 in num_vals1.values():
        return hand2, "full house"
    if is_flush(hand1):
        if is_flush(hand2):
            print("Comparing flush.  Winner by highest value is", winner_by_highest_value)
            if winner_by_highest_value == 1:
                return hand1, "flush"
            return hand2, "flush"
        return hand1, "flush"
    if is_flush(hand2):
        return hand2, "flush"
    if is_straight(hand1):
        if is_straight(hand2):
            print("Comparing straight.  Winner by highest value is", winner_by_highest_value)
            if winner_by_highest_value == 1:
                return hand1, "straight"
            return hand2, "straight"
        return hand1, "straight"
    if is_straight(hand2):
        return hand2, "straight"
    if 3 in num_vals1.values():
        if 3 in num_vals2.values():
            print("Comparing three of a kind.  Winner by highest value is", winner_by_highest_value)
            if winner_by_highest_value == 1:
                return hand1, "three of a kind"
            return hand2, "three of a kind"
        return hand1, "three of a kind"
    if 3 in num_vals2.values():
        return hand2, "three of a kind"
    if is_pair_of_pairs(num_vals1):
        if is_pair_of_pairs(num_vals2):
            print("Comparing two pairs.  Winner by highest value is", winner_by_highest_value)
            if winner_by_highest_value == 1:
                return hand1, "two pairs"
            return hand2, "two pairs"
        return hand1, "two pairs"
    if is_pair_of_pairs(num_vals2):
        return hand2, "two pairs"
    if 2 in num_vals1.values():
        print("Comparing pair 1.  Winner by highest value is", winner_by_highest_value)
        if 2 in num_vals2.values():
            print("Comparing pair 2 from pair 1.  Winner by highest value is", winner_by_highest_value)
            val1 = [valuesdictionary[val] for val in num_vals1 if num_vals1[val] == 2][0]
            val2 = [valuesdictionary[val] for val in num_vals2 if num_vals2[val] == 2][0]
            if val1 > val2:
                return hand1, "pair"
            if val2 > val1:
                return hand2, "pair"
            if winner_by_highest_value == 1:
                return hand1, "pair"
            return hand2, "pair"
        return hand1, "pair"
    if 2 in num_vals2.values():
        print("Comparing pair 2.  Winner by highest value is", winner_by_highest_value)
        return hand2, "pair"
    '''
    ...
    Comparing pair 1.  Winner by highest value is 2
    Comparing pair 2 from pair 1.  Winner by highest value is 2
    winning hand (['4C', 'KC', '3H', '7S', 'KS'], 'pair')
    Comparing pair 2.  Winner by highest value is 2
    winning hand (['4C', 'QC', 'AC', 'KH', 'QS'], 'pair')
    Comparing pair 1.  Winner by highest value is 2
    winning hand (['2D', 'JC', '2H', '5H', '6S'], 'pair')
    Comparing pair 2.  Winner by highest value is 1
    winning hand (['6D', 'AC', '3S', 'TS', 'AS'], 'pair')
    Comparing pair 1.  Winner by highest value is 2
    winning hand (['5C', 'TC', '2H', '4S', '5S'], 'pair')
    ...
    '''
    if winner_by_highest_value == 1:
        return hand1, "highest card"
    return hand2, "highest card"


count = 0

with open("0054_poker.txt") as ffileopen:
    for line in ffileopen:
        # read in the line, separating to two hands
        cards = line.strip().split(" ")
        hand1 = sort_hand(cards[:5]) #hands are sorted after reading and separting
        hand2 = sort_hand(cards[5:]) #hands are sorted after reading and separting
        #evaluate hands from the two players
        winning_hand = evaluate_winner(hand1, hand2)
        # print("hand1",hand1) #print hand1 ['8C', 'KC', '9H', '4S', 'TS']
        # print("hand2",hand2) #print hand2 ['5D', '7D', 'AC', '2S', '3S']
        print("winning hand", winning_hand) #print winning hand (['5D', '7D', 'AC', '2S', '3S'], 'highest card')
        # print("\n")
        if winning_hand[0] == hand1:
            #print("winning_hand", hand1, hand2) #print winning_hand ['8C', 'KC', '9H', '4S', 'TS'] ['5D', '7D', 'AC', '2S', '3S']
            count += 1

    ffileopen.close()

print("count variable score1 > score2", count) #print count variable score1 > score2 376.  RM:  Youtuber tested two full house hands he inputed.  Program was incorrect on the winner.
