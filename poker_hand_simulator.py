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
HAND_SIZE = 5

deck = []
for suit in SUITS:
    for rank in RANKS:
        deck.append(rank + suit)

random.shuffle(deck)
hand = deck[:HAND_SIZE]

hand_text = ''
for card in hand:
    hand_text += card + '  '
print(f"Your hand: {hand_text}")
