from __future__ import annotations
import helpers


class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    DECK = dict.fromkeys([CLUBS, DIAMONDS, HEARTS, SPADES],["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"])
    SYMBOLS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    A_VALUE = 1
    K_VALUE = 13
    MAX_CARDS = 51 #Por índice Python

    def __init__(self, value: int|str, suit: str):
        self.suit = suit
        self.value = value
        if suit not in self.DECK:
            raise InvalidCardError(message=f"{repr(suit)} is not a supported suit")
        if isinstance (self, int):
            if not 1 <= value <= 13:
                raise InvalidCardError(message=f"{repr(value)} is not a supported value")
        elif isinstance(self, str):
            if value not in self.DECK:
                raise InvalidCardError(message=f"{repr(value)} is not a supported symbol")
            self.value = self.SYMBOLS.index(value) + 1

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
        return f'{self.DECK[self.suit][self.value - 1]}{self.suit} '
    
    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

class Deck:
    LAST_CARD = 51
    FIRST_CARD = 0

    def __init__(self):
        self.cards = []
        for suit, values in Card.DECK.items():
            for value in values:
                int_value = values.index(value) + 1
                new_card = Card(int_value, suit)
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
    def __init__(self):
        ...
        
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


# card = Card(1,Card.HEARTS)
# print(card)
# deck1 = Deck()
# print(deck1.cards)
# print(deck1.get_random_card())
# print(deck1.shuffle())