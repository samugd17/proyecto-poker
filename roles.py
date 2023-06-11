from __future__ import annotations
import helpers
from cards import Deck, Card, Hand


class Player:
    def __init__(self, name: str):
        self.name = name.title()
        self.private_cards: list = []
        self.common_cards: list = []

    def __repr__(self) -> str:
        return f"{self.name} {self.private_cards}"
    
    @property
    def show_game_cards(self) -> list:
        return self.private_cards + self.common_cards
    
    def make_all_combinations(self) -> list:
        return list(helpers.combinations(self.show_game_cards, n=5))
    
    def check_possible_hands(self):
        cards= []
        for combination in self.make_all_combinations():
            sorted(combination, key=lambda card: card.value)
            for card in combination:
                cards.append(card)
        card_combinations = [cards[i:i+5] for i in range(0, len(cards), 5)]
        return card_combinations
    
    def find_best_hand(self):
        best_hand = [None, 0]
        for combination in self.check_possible_hands():         
            suits = [card.suit for card in combination]
            card_values = [card.cmp_value for card in combination]
            same_suit = len(set(suits)) == 1

            # Establecemos todas las combinaciones posibles
            straight = sorted(card_values) == list(range(min(card_values), max(card_values) + 1))
            straight_flush = same_suit and straight
            four_of_a_kind = any(card_values.count(value) == 4 for value in set(card_values))
            full_house = (any(card_values.count(value) == 3 for value in set(card_values))and len(set(card_values)) == 2)
            flush = any(suits.count(suit) == 5 for suit in set(suits))
            three_of_a_kind = any(card_values.count(value) == 3 for value in set(card_values))
            two_pairs = len(set(card_values)) == 3 and any(card_values.count(value) == 2 for value in set(card_values))
            one_pair = len(set(card_values)) == 4
            high_card = len(set(card_values)) == 5

            if straight_flush:
                actual_hand = [combination, Hand.STRAIGHT_FLUSH]
            elif four_of_a_kind:
                actual_hand = [combination, Hand.FOUR_OF_A_KIND]
            elif full_house:
                three_of_a_kind_value = max(set(card_values), key=card_values.count)
                # pair_value = min(set(card_values), key=card_values.count)
                actual_hand = [combination, Hand.FULL_HOUSE]
            elif flush:
                actual_hand = [combination, Hand.FLUSH]
            elif straight:
                actual_hand = [combination, Hand.STRAIGHT]
            elif three_of_a_kind:
                actual_hand = [combination, Hand.THREE_OF_A_KIND]
            elif two_pairs:
                # pairs_values = [value for value in set(card_values) if card_values.count(value) == 2]
                # self.cat_rank = tuple(str(value) for value in sorted(pairs_values, reverse=True))
                actual_hand = [combination, Hand.TWO_PAIR]
            elif one_pair:
                actual_hand = [combination, Hand.ONE_PAIR]
            elif high_card:
                actual_hand = [combination, Hand.HIGH_CARD]
            
            if actual_hand[1] > best_hand[1]:
                best_hand = actual_hand
        return best_hand
    
    def get_cat_rank(self) -> str | tuple[str]:
        hand, hand_cat = self.find_best_hand()
        print(hand, hand_cat)
        if hand_cat == Hand.FULL_HOUSE:
            return ""
        elif hand_cat == Hand.TWO_PAIR:
            pairs_values = [card for card in hand if hand.count(card) == 2]
            print(pairs_values)
        high_card = (max(card for card in hand))
        return high_card.str_value



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
            self.players[i].common_cards = table_cards
        return table_cards

    def give_player_cards(self):
        for i in range(len(self.players)):
            player_cards = []
            for _ in range(2):
                new_card = self.cards.get_random_card()
                player_cards.append(new_card)
                self.players[i].private_cards = player_cards

    def __repr__(self) -> str:
        return f"{self.table_cards}"
    


