from __future__ import annotations
from roles import Player, Dealer
from cards import Card, Hand, Deck


class Game:
    def __init__(self, num_players: int = 2):
        self.num_players = num_players
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.deck = Deck()
        self.dealer = Dealer(self.players)

    def start_game(self):
        self.dealer.give_player_cards()
        self.dealer.take_common_cards()

    def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
        pass


game = Game()
game.start_game()
print(game.players[0].common_cards)
print(game.players[0].private_cards)
print(game.players[1].private_cards)
print(game.players[0].find_best_hand())
print(game.players[1].find_best_hand())
print(game.players[1].get_cat_rank())
# [9♠, 8◆, A♠, 7❤, A◆]
# [K◆, K♠]