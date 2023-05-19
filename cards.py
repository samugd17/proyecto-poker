from __future__ import annotations

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

    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit
        if suit not in self.GLYPHS:
            raise InvalidCardError(message=f"{repr(suit)} is not a supported suit")
        if isinstance(value, int):
            if not (1 <= value <= 13):
                raise InvalidCardError(message=f"{repr(value)} is not a supported value")
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
        return self.GLYPHS[self.suit][self.value - 1]

class Deck:
    def __init__(self):
        ...
    
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