from collections import Counter
from card import Card


def get_card_value(card):
    return Card.get_card_value(card)  # Используется метод класса Card для получения значения


def sort_cards(cards):
    return sorted(cards, key=lambda card: get_card_value(card), reverse=True)  # sorted(iterable,key=None,reverse=False)


get_royal = ['3h', '5h', '7h', '2h', '4h', '9c', 'Ad']
sorted_cards = sort_cards(get_royal)
print(sorted_cards)
print(sorted_cards[:-1])

suits_player = [card[-1] for card in sorted_cards]
print(suits_player)
is_flush = [k for k, v in Counter(suits_player).items() if v >= 5]
print(is_flush)

if is_flush:
    flush_cards = [flush_card for flush_card in sorted_cards if flush_card[1] == is_flush[0]]
    print(800 + get_card_value(flush_cards[0]))
    print(flush_cards)
    print(f"Флэш по {flush_cards[0][0]}")
else:
    print("Флэша нету")
