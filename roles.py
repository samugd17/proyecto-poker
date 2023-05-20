from __future__ import annotations
import helpers, cards

class Player:
    def __init__(self, name: str = "Neo"):
        self.name = name
        self.cards = cards.Hand()
    ...
class Dealer:
    def __init__(self, players: str):
        self.players = players
        self.cards = cards.Deck()
