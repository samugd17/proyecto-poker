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
    A_VALUE = "A"
    MAX_CARDS = 51  # Por índice Python

    def __init__(self, card_value: str):
        self.value = card_value[0]
        self.suit = card_value[1]

        if self.suit not in self.DECK:
            raise InvalidCardError(message=f"{repr(self.suit)} is not a supported suit")
        if self.value not in self.DECK[self.suit]:
            raise InvalidCardError(
                message=f"{repr(self.value)} is not a supported value"
            )

    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras."""
        if self.value == self.A_VALUE:
            return 14
        return self.DECK[self.suit].index(self.value) + 1

    def __lt__(self, other: Card):
        return self.cmp_value < other.cmp_value

    def __gt__(self, other: Card):
        return self.cmp_value > other.cmp_value

    def __repr__(self):
        return f"{self.DECK[self.suit][self.cmp_value - 1]}{self.suit} "

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
                new_card = value + suit
                self.cards.append(new_card)

    def __getitem__(self, index: int) -> str:
        return self.cards[index]

    def get_random_card(self):
        random_value = helpers.randint(Card.MAX_CARDS)
        Card.MAX_CARDS -= 1
        return self.cards.pop(random_value)

    @property
    def view_random_card(self):
        random_value = helpers.randint(Card.A_VALUE, Card.MAX_CARDS)
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
    def __init__(self, common_cards: str, player_cards: str):
        self.game_cards = list(common_cards) + list(player_cards)

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


# card1 = Card("J♠")
# card2 = Card("K♠")
card3 = Card("A♣")
print(card3)
# print(card2.is_consecutive(card3))
deck1 = Deck()
print(deck1.cards)
# print(deck1.get_random_card())
# print(deck1.shuffle())
