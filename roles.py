from __future__ import annotations
import helpers
from cards import Deck


class Player:
    def __init__(self, name: str):
        self.name = name.title()
        self.cards = ""

    def choose_best_combination(self):
        ...

    def __repr__(self) -> str:
        return f"{self.name}: {self.cards}"


class Dealer:
    def __init__(self, *players: Player):
        self.players = players
        self.cards = Deck()
        self.table_cards = self.take_common_cards()

    def take_common_cards(self):
        table_cards = ""
        for _ in range(5):
            new_card = str(self.cards.get_random_card())
            table_cards += new_card
        return table_cards

    def give_player_cards(self):
        player_cards = ""
        for _ in range(2):
            new_card = str(self.cards.get_random_card())
            player_cards += new_card
        return player_cards

    def __repr__(self) -> str:
        return f"Board: {self.table_cards}"


player = Player("samu")
player1 = Player("lolo")
print(player)
print(player1)

dealer = Dealer(player, player1)
print(dealer)
