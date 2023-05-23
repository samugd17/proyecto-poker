from __future__ import annotations
import helpers


class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    GLYPHS = {
        CLUBS: "🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞",
        DIAMONDS: "🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎",
        HEARTS: "🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾",
        SPADES: "🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮",
    }
    A_VALUE = 1
    K_VALUE = 13
    MAX_CARDS = 51

    def __init__(self, value: int, suit: str):
        if suit not in self.GLYPHS:
            raise InvalidCardError(message=f"{repr(suit)} is not a supported suit")
        if not 1 <= value <= 13:
            raise InvalidCardError(message=f"{repr(value)} is not a supported value")
        self.suit = suit
        self.value = value

    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS."""
        if self.value == Card.A_VALUE:
            self.value = 14
        return self.value

    def __lt__(self, other: Card):
        return self.cmp_value < other.value

    def __repr__(self):
        """Devuelve el glifo de la carta"""
        return f'{self.GLYPHS[self.suit][self.value - 1]} '

class Deck:
    LAST_CARD = 51
    FIRST_CARD = 0

    def __init__(self):
        self.cards = []
        for suit, values in Card.GLYPHS.items():
            for value in values:
                int_value = values.index(value) + 1
                new_card = Card(int_value, suit)
                self.cards.append(new_card)
                
    def __getitem__(self, index: int) -> str:
        return self.cards[index]

    def get_random_card(self):
        random_value = helpers.randint(Card.A_VALUE, Card.MAX_CARDS)
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
    def __init__(self):
        ...


class InvalidCardError(Exception):
    def __init__(self, *, message: str = ""):
        default_message = "🃏 Invalid card"
        if not message:
            self.message = default_message
        else:
            self.message = f"{default_message}: {message}"
        super().__init__(self.message)


# card = Card(1,Card.HEARTS)
# print(card)
deck1 = Deck()
# print(deck1.cards)
print(deck1.get_random_card())
# print(deck1.shuffle())