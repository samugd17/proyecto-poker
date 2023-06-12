from __future__ import annotations
import helpers
from cards import Deck, Hand


class Player:
    def __init__(self, name: str):
        self.name = name.title()
        self.private_cards: list = []
        self.common_cards: list = []

    def __repr__(self) -> str:
        return f"{self.private_cards}"

    @property
    def show_game_cards(self) -> list:
        return self.private_cards + self.common_cards

    def make_all_combinations(self) -> list:
        return list(helpers.combinations(self.show_game_cards, n=5))

    def check_possible_hands(self):
        cards = []
        for combination in self.make_all_combinations():
            for card in combination:
                cards.append(card)
        card_combinations = [cards[i : i + 5] for i in range(0, len(cards), 5)]
        return card_combinations

    def find_best_hand(self):
        best_hand = [None, 0]
        for combination in self.check_possible_hands():
            suits = [card.suit for card in combination]
            card_values = [card.cmp_value for card in combination]
            same_suit = len(set(suits)) == 1

            # Establecemos todas las combinaciones posibles
            straight = sorted(card_values) == list(
                range(min(card_values), max(card_values) + 1)
            )
            straight_flush = same_suit and straight
            four_of_a_kind = any(
                card_values.count(value) == 4 for value in set(card_values)
            )
            full_house = (
                any(card_values.count(value) == 3 for value in set(card_values))
                and len(set(card_values)) == 2
            )
            flush = same_suit
            three_of_a_kind = any(
                card_values.count(value) == 3 for value in set(card_values)
            )
            two_pairs = len(set(card_values)) == 3 and any(
                card_values.count(value) == 2 for value in set(card_values)
            )
            one_pair = len(set(card_values)) == 4
            high_card = len(set(card_values)) == 5

            if straight_flush:
                actual_hand = [combination, Hand.STRAIGHT_FLUSH]
            elif four_of_a_kind:
                actual_hand = [combination, Hand.FOUR_OF_A_KIND]
            elif full_house:
                actual_hand = [combination, Hand.FULL_HOUSE]
            elif flush:
                actual_hand = [combination, Hand.FLUSH]
            elif straight:
                actual_hand = [combination, Hand.STRAIGHT]
            elif three_of_a_kind:
                actual_hand = [combination, Hand.THREE_OF_A_KIND]
            elif two_pairs:
                actual_hand = [combination, Hand.TWO_PAIR]
            elif one_pair:
                actual_hand = [combination, Hand.ONE_PAIR]
            elif high_card:
                actual_hand = [combination, Hand.HIGH_CARD]

            if actual_hand[1] > best_hand[1]:
                best_hand = actual_hand
            elif actual_hand[1] == best_hand[1]:
                n1 = sum(i.cmp_value for i in actual_hand[0])
                n2 = sum(i.cmp_value for i in best_hand[0])
                if n1 > n2:
                    best_hand = actual_hand
        return best_hand

    def get_cat_rank(self) -> str | tuple[str]:
        hand_cards, hand_cat = self.find_best_hand()
        pairs_values = list(
            set(card.str_value for card in hand_cards if hand_cards.count(card) == 2)
        )
        three_of_a_kind_value = list(
            set(card.str_value for card in hand_cards if hand_cards.count(card) == 3)
        )
        four_of_a_kind_value = list(
            set(card.str_value for card in hand_cards if hand_cards.count(card) == 4)
        )

        if hand_cat == Hand.FOUR_OF_A_KIND:
            return four_of_a_kind_value[0]
        if hand_cat == Hand.FULL_HOUSE:
            return tuple(three_of_a_kind_value + pairs_values)
        if hand_cat == Hand.THREE_OF_A_KIND:
            return three_of_a_kind_value[0]
        if hand_cat == Hand.TWO_PAIR:
            formatted_pairs_values = sorted(pairs_values, reverse=True)
            return tuple(formatted_pairs_values)
        if hand_cat == Hand.ONE_PAIR:
            return pairs_values[0]
        high_card = max(card for card in hand_cards)
        return high_card.str_value

    def build_hand(self) -> Hand:
        cards, cat = self.find_best_hand()
        new_hand = Hand(cards)
        new_hand.cat = cat
        new_hand.cat_rank = self.get_cat_rank()
        return new_hand


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
