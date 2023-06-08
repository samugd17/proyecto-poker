from __future__ import annotations
import helpers


class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    DECK = dict.fromkeys(
        [CLUBS, DIAMONDS, HEARTS, SPADES],
        ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
    )
    INIT_A_VALUE = 1
    HIGHEST_A_VALUE = 14
    MAX_CARDS = 51  # Por índice Python

    def __init__(self, card_value: str):
        self.value = card_value[:-1]
        self.suit = card_value[-1]

        if self.suit not in self.DECK:
            raise InvalidCardError(message=f"{repr(self.suit)} is not a supported suit")
        if self.value not in self.DECK[self.suit]:
            raise InvalidCardError(message=f"{repr(self.value)} is not a supported value")

    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras."""
        if self.value == "A":
            return self.HIGHEST_A_VALUE
        return self.DECK[self.suit].index(self.value) + 1

    def __lt__(self, other: Card):
        return self.cmp_value < other.cmp_value

    def __gt__(self, other: Card):
        return self.cmp_value > other.cmp_value

    def __repr__(self):
        return f"{self.value}{self.suit}"

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def same_value(self, other: Card):
        return self.value == other.value

    def same_suit(self, other: Card):
        return self.suit == other.suit

    def is_consecutive(self, other: Card):
        if self.cmp_value > other.cmp_value:
            return self.cmp_value - other.cmp_value == 1
        return other.cmp_value - self.cmp_value == 1


class Deck:
    LAST_CARD = 51
    FIRST_CARD = 0

    def __init__(self):
        self.cards = []
        for suit, values in Card.DECK.items():
            for value in values:
                new_card = Card(value + suit)
                self.cards.append(new_card)

    def __getitem__(self, index: int) -> str:
        return self.cards[index]

    def get_random_card(self):
        random_value = helpers.randint(Card.MAX_CARDS)
        Card.MAX_CARDS -= 1
        return self.cards.pop(random_value)

    @property
    def view_random_card(self):
        random_value = helpers.randint(Card.MAX_CARDS)
        return self.cards[random_value]

    def get_top_card(self):
        return self.cards.pop(self.FIRST_CARD)

    def get_bottom_card(self):
        return self.cards.pop(self.LAST_CARD)

    @property
    def view_top_card(self):
        return self.cards[self.FIRST_CARD]

    @property
    def view_bottom_card(self):
        return self.cards[self.LAST_CARD]

    def shuffle(self):
        helpers.shuffle(self.cards)
        return self.cards


class Hand:
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

    def __init__(self, common_cards: list[Card], player_cards: list[Card]):
        self.game_cards = common_cards + player_cards
        self.cat = 0
        self.cat_rank: str | tuple = None

    def __contains__(self, b):
        return self in b

    def make_all_combinations(self):
        return list(helpers.combinations(self.game_cards, n=5))
    
    def check_hand(self) -> None:
        suits = [card.suit for card in self.game_cards]
        card_values = [card.cmp_value for card in self.game_cards]
        same_suit = len(set(suits)) == 1

        # Establecemos todas las combinaciones posibles
        straight = sorted(card_values) == list(range(min(card_values), max(card_values) + 1))
        straight_flush = same_suit and straight
        four_of_a_kind = any(card_values.count(value) == 4 for value in set(card_values))
        full_house = any(card_values.count(value) == 3 for value in set(card_values)) and len(set(card_values)) == 2
        flush = any(suits.count(suit) == 5 for suit in set(suits))
        three_of_a_kind = any(card_values.count(value) == 3 for value in set(card_values))
        two_pairs = len(set(card_values)) == 3 and any(card_values.count(value) == 2 for value in set(card_values))
        one_pair = len(set(card_values)) == 4
        high_card = max(card_values)

        self.possible_categories = [straight, straight_flush, four_of_a_kind, full_house, flush, three_of_a_kind, two_pairs, one_pair, high_card]

        # Determinamos la categoría y rango de la mano
        if straight_flush:
            self.cat = self.STRAIGHT_FLUSH
            self.cat_rank = str(max(card_values))
        elif four_of_a_kind:
            self.cat = self.FOUR_OF_A_KIND
            self.cat_rank = str(max(card_values))
        elif full_house:
            three_of_a_kind_value = max(set(card_values), key=card_values.count)
            pair_value = min(set(card_values), key=card_values.count)
            self.cat = self.FULL_HOUSE
            self.cat_rank = tuple(str(three_of_a_kind_value), str(pair_value))
        elif flush:
            self.cat = self.FLUSH
            self.cat_rank = str(max(card_values))
        elif straight:
            self.cat = self.STRAIGHT
        elif three_of_a_kind:
            self.cat = self.THREE_OF_A_KIND
            self.cat_rank = str(max(card_values))
        elif two_pairs:
            pairs_values = [value for value in set(card_values) if card_values.count(value) == 2]
            self.cat = self.TWO_PAIR
            self.cat_rank = tuple(str(value) for value in sorted(pairs_values, reverse=True))
        elif one_pair:
            self.cat = self.ONE_PAIR
            self.cat_rank = str(max(card_values))
        else:
            self.cat = self.HIGH_CARD
            self.cat_rank = str(max(card_values))

class InvalidCardError(Exception):
    def __init__(self, *, message: str = ""):
        default_message = "🃏 Invalid card"
        if not message:
            self.message = default_message
        else:
            self.message = f"{default_message}: {message}"
        super().__init__(self.message)


# card1 = Card("Q♣")
# card2 = Card("A♣")
# card3 = Card("10♣")
# print(card1)
# deck1 = Deck()
# print(deck1.cards)
# print(deck1.get_random_card())
# print(deck1.shuffle())



