import random
from itertools import chain 

num = {'♣': ['🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃝', '🃞'],
'◆': ['🃁', '🃂', '🃃' ,'🃄' ,'🃅' ,'🃆' ,'🃇' ,'🃈' ,'🃉' ,'🃊' ,'🃋' ,'🃍' ,'🃎'],
'❤': ['🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂽', '🂾'],
'♠': ['🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂭', '🂮']}

def cards():
    mix = []
    for _ in num.values():
        random.shuffle(_)
        mix.append(_)
    encapsulator = list(chain(*mix))
    return encapsulator.pop(0)
    
print(cards())

# caso de prueba para generar las cartas de la mesa.

#def cards():
#    bolsa = []
#    for i in num.values():
#        a = random.choice(i)
#        bolsa.append(a)
#        continue
#    return bolsa
#cards()