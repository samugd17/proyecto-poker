import re

regex = r'♣{5}|◆{5}|❤{5}|♠{5}'
p1 = '♣◆❤♠♣◆❤♠'
p2 = '◆◆◆◆◆'
res = 'Lesgo'if re.match(regex, p2) is not None else 'No'

total_cards = [1, 2, 4, 6, 8, 9]

rep_cards = list(str(Card) for Card in total_cards)
print(rep_cards)