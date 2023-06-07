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
        if len(card_value) > 2:
            self.value = card_value[:2]
            self.suit = card_value[2]
        else:
            self.value = card_value[0]
            self.suit = card_value[1]

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
        return f"{self.value}{self.suit} "

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
        self.cat = ""
        self.cat_rank = ""

    def __contains__(self):
        ...

    def choose_best_combination(self):
        # helpers.combinations(cards.Hand(), 5)
        pass


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
