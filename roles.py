from __future__ import annotations
import helpers, cards

class Player:
    def __init__(self):
        name = input("Introduce tu nombre: ").title()
        self.name = name
        self.cards = cards.Hand()
    ...
class Dealer:
    def __init__(self, *players: Player):
        self.players = players
        self.cards = cards.Deck()
    
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

player = Player()
player1 = Player()
print(player.name)
print(player1.name)

dealer1 = Dealer(player,player1)
print(dealer1.give_player_cards())
print(dealer1.take_common_cards())