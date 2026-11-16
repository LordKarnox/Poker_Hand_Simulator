"""
Program: Poker Hand Simulator
Author: Boston Deevech
Date: November 15, 2026

Purpose: Deal 5-card poker hands from a shuffled 52-card deck, identify
each hand's rank, track chips and statistics across rounds, and keep
running until the user chooses to quit.
"""

import random

SUITS = ('♠', '♥', '♦', '♣')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
RANK_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14,
}
HAND_SIZE = 5

deck = []
for suit in SUITS:
    for rank in RANKS:
        deck.append(rank + suit)

random.shuffle(deck)
hand = deck[:HAND_SIZE]

rank_counts = {}
suit_counts = {}
values = []
for card in hand:
    rank = card[:-1]
    suit = card[-1]
    rank_counts[rank] = rank_counts.get(rank, 0) + 1
    suit_counts[suit] = suit_counts.get(suit, 0) + 1
    values.append(RANK_VALUES[rank])
values.sort()
match_counts = sorted(rank_counts.values(), reverse=True)

is_flush = len(suit_counts) == 1
is_straight = False
if len(rank_counts) == HAND_SIZE:
    if values[-1] - values[0] == HAND_SIZE - 1:
        is_straight = True
    # The ace also counts low, so A-2-3-4-5 is a straight.
    elif values == [2, 3, 4, 5, 14]:
        is_straight = True

if is_flush:
    hand_rank = 'Flush'
elif is_straight:
    hand_rank = 'Straight'
elif match_counts[0] == 4:
    hand_rank = 'Four of a Kind'
elif match_counts[0] == 3:
    hand_rank = 'Three of a Kind'
elif match_counts[:2] == [2, 2]:
    hand_rank = 'Two Pair'
elif match_counts[0] == 2:
    hand_rank = 'Pair'
else:
    hand_rank = 'High Card'

hand_text = ''
for card in hand:
    hand_text += card + '  '
print(f"Your hand: {hand_text}")
print(f"Result: {hand_rank}")
