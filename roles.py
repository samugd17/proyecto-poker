from __future__ import annotations
from cards import Deck

cards_random = Deck.card_random()

class Player:
    def __init__(self, name="Neo"):
        self.name = name
        self.cards_random = cards_random()

    def card_player_private(self):
        return self.cards_random()[0:2]
    
class Dealer:
    def __init__(self, players: str):
        ...

a = Player()
print(a.card_player_private())
