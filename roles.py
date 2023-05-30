from __future__ import annotations
import helpers, cards


class Player:
    def __init__(self, name: str):
        self.name = name.title()
        self.cards = ""
    def choose_best_combination(self, other: Dealer):
        total_cards = self.cards + other.table_cards
        combinations = list(helpers.combinations(total_cards, n = 5))
        
        pass
        
class Dealer:
    def __init__(self, *players: Player):
        self.players = players
        self.cards = cards.Deck()
        self.table_cards = self.take_common_cards()

    def take_common_cards(self):
        table_cards = ""
        for _ in range(5):
            new_card = str(self.cards.get_random_card())
            table_cards += new_card
        return table_cards

    def give_player_cards(self, other: Player): 
        for _ in range(2):
            new_card = str(self.cards.get_random_card())
            other.cards += new_card
        return other.cards
    



player = Player("samu")
player1 = Player("lolo")
print(player.name)
print(player1.name)

dealer1 = Dealer(player, player1)
print(dealer1.give_player_cards(player))
print(player.cards)
print(dealer1.take_common_cards())

player.choose_best_combination(dealer1)