from __future__ import annotations
import helpers
from cards import Deck, Card, Hand


class Player:
    def __init__(self, name: str):
        self.name = name.title()
        self.cards: list = []
        self.table_cards: list = []

    def __repr__(self) -> str:
        return f"{self.name} {self.cards}"
    
    def find_best_hand(self):
        player_hand = Hand(self.table_cards, self.cards)
        print(player_hand.check_hand())


class Dealer:
    def __init__(self, players: list[Player]):
        self.players = players
        self.cards = Deck()
        self.table_cards = self.take_common_cards()

    def take_common_cards(self):
        table_cards = []
        for _ in range(5):
            new_card = self.cards.get_random_card()
            table_cards.append(new_card)
        
        for i in range(len(self.players)):
            self.players[i].table_cards = table_cards
        
        return table_cards
    

    def give_player_cards(self):
        for i in range(len(self.players)):
            player_cards = []
            for _ in range(2):
                new_card = self.cards.get_random_card()
                player_cards.append(new_card)
                self.players[i].cards = player_cards

    def __repr__(self) -> str:
        return f"Board {self.table_cards}"
