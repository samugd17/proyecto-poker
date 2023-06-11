from __future__ import annotations
from roles import Player, Dealer
from cards import Card, Hand, Deck

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
    for i, player in enumerate(players):
        player.private_cards, player.common_cards = private_cards[i], common_cards

    winners = []
    best_hand = None
    for player in players:
        player_hand = player.build_hand()
        if best_hand is None or player_hand > best_hand:
            best_hand = player_hand
            winners = [player]
        elif player_hand == best_hand:
            winners.append(player)

    if len(winners) == 1:
        return winners[0], best_hand
    else:
        return None, best_hand

# game = Game()
# game.start_game()
# print(game.players[0].common_cards)
# print(game.players[0].private_cards)
# print(game.players[1].private_cards)
# print(game.players[0].find_best_hand())
# print(game.players[1].find_best_hand())
# print(game.players[0].get_cat_rank())
# print(game.players[1].get_cat_rank())
# players = [Player('Player 1'), Player('Player 2')]
# common_cards = [Card('A◆'), Card('J❤'), Card('9◆'), Card('8❤'), Card('8♣')]
# private_cards = [[Card('10♣'), Card('10❤')], [Card('5♣'), Card('2❤')]]
# print(get_winner(players, common_cards, private_cards))

