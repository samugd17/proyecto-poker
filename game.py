from __future__ import annotations
from roles import Player, Dealer
from cards import Card, Hand, Deck

class Game:
    def __init__(self, num_players: int = 2):
        self.num_players = num_players
        self.deck = Deck()
        self.dealer = Dealer()
        self.players = Player()
        ...
    
def get_winner(
    players: list[Player],
    common_cards: list[Card],
    private_cards: list[list[Card]],
) -> tuple[Player | None, Hand]:
