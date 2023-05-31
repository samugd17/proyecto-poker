import random

cards = {"♣":"🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞",
"◆":"🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎",
"❤":"🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾",
"♠":"🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮"}

class Deck:

    def __init__(self, cards: dict|str):
        self.cards = cards

    def list_palo(self):
        palo = cards.values()
        lista_palo = list(palo)
        troceado = list(lista_palo[0])
        return troceado
        
    def randoms(self):
        palo_lista = self.list_palo
        return random.shuffle(palo_lista)
    
deck = Deck(cards)
deck.randoms()