"""
If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

# ordered card ranking list
CARD_RANKINGS = range(1, 15)


def get_card_ranking(card):
    """given a card, eg "QD" queen of diamonds, return it's rank
    """
    valMap = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    card_val = card[0]
    if card_val in valMap:
        card_val = valMap[card_val]
    else:
        card_val = int(card_val)
    return card_val


assert get_card_ranking("QD") == 12
assert get_card_ranking("1D") == 1


def rank_hand(cards):
    """
        0. high card
        1. one pair
        2. two pairs
        3. three of a kind
        4. straight
        5. flush
        6. full house
        7. four of a kind
        8. straight flush
        9. royal flush

        return a tuple with the highest rank of the hand,
        the descending sorted values of the cards associated with the rank (for tie breaker)
        and the descending sorted card_rankings (for 2nd tie breaker)
    """
    # card rankings from the cards, ignore suit
    card_rankings = [get_card_ranking(c) for c in cards]
    card_rankings = sorted(card_rankings, reverse=True)

    # count up the number of instances of each card in the player's hand
    card_counts = dict.fromkeys(CARD_RANKINGS, 0)
    for r in card_rankings:
        card_counts[r] += 1
    card_counts_list = sorted(card_counts.values(), reverse=True)

    # find whether they're all the same suit
    flush = len(set([c[1] for c in cards])) == 1

    # find out whether they're ascending as a straight
    straight = True
    for i, c in enumerate(card_rankings[1:], 1):
        if c != card_rankings[i - 1] - 1:
            straight = False

    max_rank = 0  # 0. we start out at high card
    ranked_cards = []

    if card_counts_list[0] > 1:
        # 1. one pair
        max_rank = 1
        ranked_cards = [c for c in card_counts if card_counts[c] > 1]
    if card_counts_list[0] > 1 and card_counts_list[1] > 1:
        # 2. two pair
        max_rank = 2
        ranked_cards = sorted(
            [c for c in card_counts if card_counts[c] > 1], reverse=True)
    if card_counts_list[0] > 2:
        # 3. three of a kind
        max_rank = 3
        ranked_cards = sorted(
            [c for c in card_counts if card_counts[c] > 2], reverse=True)
    if straight:
        # straight
        max_rank = 4
        ranked_cards = card_rankings
    if flush:
        # flush
        max_rank = 5
        ranked_cards = card_rankings
    if card_counts_list[0] == 3 and card_counts_list[1] == 2:
        # full house
        max_rank = 6
        ranked_cards = [c for c in card_counts if card_counts[c] == 3
                        ] + [c for c in card_counts if card_counts[c] == 2]
    if card_counts_list[0] == 4:
        # four of a kind
        max_rank = 7
        ranked_cards = [c for c in card_counts if card_counts[c] > 3]
    if straight and flush:
        # straight flush
        max_rank = 8
        ranked_cards = card_rankings
    if straight and flush and card_rankings[0] == 14:
        # royal straight flush
        max_rank = 9
        ranked_cards = card_rankings

    return (max_rank, ranked_cards, card_rankings)


assert rank_hand(["TC", "JC", "QC", "KC", "AC"])[0] == 9


def player_1_wins_hand(cards):
    """
        given the cards, rank them, compare for tie breakers, and return
        a boolean for whether player one has won the current/tested hand
    """
    if (type(cards) is not list):
        # for testing purposes
        cards = cards.split(" ")

    player_1_hand = rank_hand(cards[:5])
    player_2_hand = rank_hand(cards[5:])
    if player_1_hand[0] > player_2_hand[0]:
        # player one has a greater hand
        return True
    elif player_1_hand[0] < player_2_hand[0]:
        return False
    elif player_1_hand[0] == player_2_hand[0]:
        # same hand, look for high card within the ranked cards
        for i, ranked_card_value in enumerate(player_1_hand[1]):
            if ranked_card_value > player_2_hand[1][i]:
                # won on high card
                return True
            elif ranked_card_value < player_2_hand[1][i]:
                # lost on high card
                return False

        # same hand, and same value cards in the ranked cards
        # loop for the highest card among the unranked cards
        for i, ranked_card_value in enumerate(player_1_hand[2]):
            if ranked_card_value > player_2_hand[2][i]:
                # won on high card
                return True
            elif ranked_card_value < player_2_hand[2][i]:
                # lost on high card
                return False
    raise RuntimeError("Dead code reached. Un-tiebroken hand...")


assert player_1_wins_hand("5H 5C 6S 7S KD 2C 3S 8S 8D TD") == False
assert player_1_wins_hand("5D 8C 9S JS AC 2C 5C 7D 8S QH") == True
assert player_1_wins_hand("2D 9C AS AH AC 3D 6D 7D TD QD") == False
assert player_1_wins_hand("4D 6S 9H QH QC 3D 6D 7H QD QS") == True
assert player_1_wins_hand("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D") == True


def poker_hands(list_of_hands=None):
    """
        for each hand/line, rank the results for the first 5 (player 1) and the last 5 (player 2)
        count if player 1 wins
    """
    poker_hands = list_of_hands
    player_1_wins = 0

    if poker_hands is None:
        poker_hands = []
        with open("54.input.txt") as poker_file:
            for hand in poker_file:
                poker_hands.append(hand.split(" "))

    for cards in poker_hands:
        if player_1_wins_hand(cards):
            player_1_wins += 1
    return player_1_wins


# output: 376 in 0.081 seconds
print(poker_hands())
