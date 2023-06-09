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
        for comb in player_hand.make_all_combinations():
            hand_comb = Hand(comb)
            hand_comb.check_hand()
        return hand_comb.cat


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
        return f"{self.table_cards}"
    
    def resolv(self):
        players_best_hand = []
        for i in range(len(self.players)):
            player_hand = self.players[i].find_best_hand()
            players_best_hand.append(player_hand)
            best_hand = max(players_best_hand)
        if players_best_hand.count(best_hand) == 1:
            return best_hand   
        return None


