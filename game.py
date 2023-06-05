from __future__ import annotations
import cards, roles



class Game:
    def __init__(self, num_players: int = 2):
        self.num_players = num_players
        self.deck = cards.Deck()
        self.dealer = roles.Dealer()
        self.players = roles.Player()
        ...

