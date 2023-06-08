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
    def __init__(self, table_cards: list[Card], own_cards: list[Card]):
        self.total_cards = table_cards + own_cards
        self.rep_cards = list(str(Card) for Card in self.total_cards)
        self.values = sorted(list(Card.cmp_value for Card in self.total_cards))
        self.suits = list(Card.suit for Card in self.total_cards)
        self.cat = ...
        self.cat_rank = ...

    def check_flush(self):
        regex = r'♣{5}|◆{5}|❤{5}|♠{5}'
        return re.match(regex, self.suits) is not None
            

    def check_straight(self):
        straight = []
        last_value = self.values[0]
        for value in self.values[1:]:
            if value == last_value + 1:
                straight.append(value)
                last_value = value
        straight.insert(0, self.values[0])
        return len(straight) >= 5
           
    def check_same_kind(self):
         for card in self.total_cards:
             if self.values.count(card.value) == 4:
                return card.value, 4
             if self.values.count(card.value) == 3:
                self.check_full_house(card)
                return card.value, 3
             if self.values.count(card.value) == 2:
                return card.value, 2
             
    def check_full_house(self, three_of_a_kind_card):
        for card in self.total_cards:
            return self.values.count(card.value) == 2 and card != three_of_a_kind_card
                
                
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