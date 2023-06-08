import re

regex = r'♣{5}|◆{5}|❤{5}|♠{5}'
p1 = '♣◆❤♠♣◆❤♠'
p2 = '◆◆◆◆◆'
res = 'Lesgo'if re.match(regex, p2) is not None else 'No'

total_cards = [1, 2, 4, 6, 8, 9]

rep_cards = list(str(Card) for Card in total_cards)
print(rep_cards)

values = total_cards = [1, 2, 1, 1, 1, 4, 4, 6, 8, 9]

same_kind = {val:values.count(val) for val in values}
print(max(same_kind.values()))