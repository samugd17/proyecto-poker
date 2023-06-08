from __future__ import annotations
import re

class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    GLYPHS = {"♣":"🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞",
"◆":"🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎",
"❤":"🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾",
"♠":"🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮"}
    A_VALUE = 1

    def __init__(self, card: str):
        self.value = card[:-1]
        self.suit = card[-1]

        if self.suit not in self.GLYPHS:
            raise InvalidCardError(message=f"{repr(self.suit)} is not a supported suit")
        if isinstance(self.value, int):
            if not (1 <= self.value <= 13):
                raise InvalidCardError(message=f"{repr(self.value)} is not a supported value")
        self.value = self.value

    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS."""
        match self.value:
            case Card.A_VALUE:
                self.value = 14
            case 'K':
                self.value = 13
            case 'Q':
                self.value = 12
            case 'J':
                self.value = 11
            case _:
                self.value = int(self.value)
        return self.value
    
    def __lt__(self, other: Card):
        return self.cmp_value < other.value

    def __repr__(self):
        """Devuelve el glifo de la carta"""
        return f'{self.cmp_value}{self.suit}'

class Deck:
    def __init__(self):
        ...
    
# Lista de las representaciones de las cartas
class Hand:       
    def __init__(self, table_cards: list, own_cards: list):
        self.total_cards = table_cards + own_cards
        rep_cards = list(str(Card) for Card in self.total_cards)
        self.cat = ...
        self.cat_rank = ...

    def check_flush(self):
        regex = r'♣{5}|◆{5}|❤{5}|♠{5}'
        cards = ''.join(self.total_cards)
        if re.match(regex, cards) is not None:
            return 'FLUSH'

    def check_straight(self):
        

    def check_same_kind(self):
        pass

    def check_highest_value(self, combination: str):
        pass

    def find_best_combination(self, value: str | int, suit: str):
        flush = self.check_flush()
        straight = self.check_straight()
        same_kind = self.same_kind()


class InvalidCardError(Exception):
    def __init__(self, *, message: str = ""):
        default_message = "🃏 Invalid card"
        if not message:
            self.message = default_message
        else:
            self.message = f"{default_message}: {message}"
        super().__init__(self.message)