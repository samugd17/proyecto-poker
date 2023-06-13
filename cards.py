from __future__ import annotations
import helpers

CLUBS = "♣"
DIAMONDS = "◆"
HEARTS = "❤"
SPADES = "♠"
DECK = dict.fromkeys(
    [CLUBS, DIAMONDS, HEARTS, SPADES],
    ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
)

CARD_VALUES = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
}

HIGHEST_A_VALUE = 14
MAX_CARDS = 51  # Por índice Python


class Card:
    def __init__(self, card_value: str):
        self.value = card_value[:-1]
        self.suit = card_value[-1]

        if self.suit not in DECK:
            raise InvalidCardError(message=f"{repr(self.suit)} is not a supported suit")
        if self.value not in DECK[self.suit]:
            raise InvalidCardError(
                message=f"{repr(self.value)} is not a supported value"
            )

    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras."""
        if self.value == "A":
            return HIGHEST_A_VALUE
        return DECK[self.suit].index(self.value) + 1

    def __lt__(self, other: Card):
        return self.cmp_value < other.cmp_value

    def __gt__(self, other: Card):
        return self.cmp_value > other.cmp_value

    def __repr__(self):
        return f"{self.value}{self.suit}"

    def __eq__(self, other):
        return self.cmp_value == other.cmp_value


class Deck:
    LAST_CARD = 51
    FIRST_CARD = 0

    def __init__(self):
        self.cards = []
        for suit, values in DECK.items():
            for value in values:
                new_card = Card(value + suit)
                self.cards.append(new_card)

    def __getitem__(self, index: int) -> str:
        return self.cards[index]

    @property
    def view_random_card(self):
        random_value = helpers.randint(MAX_CARDS)
        return self.cards[random_value]

    def get_random_card(self):
        random_value = helpers.randint(self.LAST_CARD)
        self.LAST_CARD -= 1
        return self.cards.pop(random_value)

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

    def __init__(self, hand: list[Card]):
        self.hand = hand
        self.cat: int = 0
        self.cat_rank: str | tuple[str] = None

    def __contains__(self, card: Card):
        return card in self.hand

    def __getitem__(self, index: int) -> Card:
        return self.hand[index]

    def __len__(self) -> int:
        return len(self.hand)

    def __repr__(self) -> str:
        return " ".join(str(card) for card in self.hand)

    def __gt__(self, other):
        same_hand = self.cat_rank == other.cat_rank and self.cat == other.cat
        if same_hand:
            return sum([card.cmp_value for card in self.hand]) > sum(
                [card.cmp_value for card in other.hand]
            )
        if self.cat > other.cat:
            return True
        return self.cat == other.cat and self.cat_rank > other.cat_rank

    def __eq__(self, other):
        if self.cat_rank == other.cat_rank and self.cat == other.cat:
            return sum([card.cmp_value for card in self.hand]) == sum(
                [card.cmp_value for card in other.hand]
            )
        return False


class InvalidCardError(Exception):
    def __init__(self, *, message: str = ""):
        default_message = "🃏 Invalid card"
        if not message:
            self.message = default_message
        else:
            self.message = f"{default_message}: {message}"
        super().__init__(self.message)
