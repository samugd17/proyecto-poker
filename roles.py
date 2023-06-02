from __future__ import annotations
import helpers, cards


class Player:
    def __init__(self, name: str):
        self.name = name.title()
        self.cards = Dealer().give_player_cards()

    def choose_best_combination(self):
        helpers.combinations(cards.Hand(), 5)
        
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

    def give_player_cards(self):
        player_cards = ""
        for _ in range(2):
            new_card = str(self.cards.get_random_card())
            player_cards += new_card
        return player_cards

player = Player("samu")
player1 = Player("lolo")
print(player.name)
print(player1.name)
print(player.cards)
print(player1.cards)

dealer1 = Dealer(player, player1)
print(dealer1.take_common_cards())
