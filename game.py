from __future__ import annotations
from roles import Player
from cards import Card, Hand

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
    for i, player in enumerate(players):
        player.private_cards, player.common_cards = private_cards[i], common_cards

    best_hand = None
    for player in players:
        player_hand = player.build_hand()
        print(player_hand)
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
# print(players[0].common_cards)
# print(players[0].private_cards)
# print(game.players[1].private_cards)
#  print(game.players[0].find_best_hand())
# print(game.players[1].find_best_hand())
# print(game.players[0].get_cat_rank())
# print(game.players[1].get_cat_rank())

players = [Player('Player 1'), Player('Player 2')]
# common_cards = [Card('A◆'), Card('J❤'), Card('8♣'), Card('7♣'), Card('6♠')]
# private_cards = [[Card('4♣'), Card('2❤')], [Card('9♠'), Card('2◆')]]
# common_cards = [Card('A◆'), Card('Q♠'), Card('Q◆'), Card('10◆'), Card('4◆')]
# private_cards = [[Card('Q❤'), Card('4♣')], [Card('6◆'), Card('2◆')]]
common_cards = [Card('Q♣'), Card('Q♠'), Card('9♣'), Card('7♠'), Card('5♠')]
private_cards = [[Card('A♠'), Card('3◆')], [Card('J♣'), Card('2♠')]]
print(get_winner(players, common_cards, private_cards))
print(players[0].private_cards)
print(players[1].private_cards)
print(players[0].find_best_hand())
print(players[1].find_best_hand())
