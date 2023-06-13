from __future__ import annotations
from roles import Player
from cards import Card, Hand

def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
    for i, player in enumerate(players):
        player.private_cards, player.common_cards = private_cards[i], common_cards

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