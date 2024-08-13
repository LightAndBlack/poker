from collections import Counter
from card import Card


# определяю значения рангов карт, чтобы отсортировать 7 карт по убыванию на основании значений рангов
# def get_card_value(card):
#     return Card.get_card_value(card)  # Используется метод класса Card для получения значения


# sorted(iterable,key=None,reverse=False)
def sort_cards(cards):
    return sorted(cards, key=lambda card: Card.get_card_value(card), reverse=True)


showdown_cards = ['6h', 'Kc', '5h', '7c', '4h', '3h', '2h']
sorted_cards = sort_cards(showdown_cards)  # начальная сортировка карт по рангу
print(sorted_cards)

# Определяю флэш
suits_player = [card[-1] for card in sorted_cards]
print(suits_player)
is_flush = [k for k, v in Counter(suits_player).items() if v >= 5]
print(is_flush)

if is_flush:
    flush_cards = [flush_card for flush_card in sorted_cards if flush_card[1] == is_flush[0]]
    print(800 + Card.get_card_value(flush_cards[0]))
    print(flush_cards)
    print(f"Флэш по {flush_cards[0][0]}")
else:
    print("Флэша нету")
# конец проверки на флэш и определение силы флэша

# Определяю стрит
straights = [
        'A2345', '23456', '34567', '45678', '56789', '678910',
        '78910J', '8910JQ', '910JQK', '10JQKA'
    ]


def is_straight():
    unique_ranks = set([rank[0] for rank in showdown_cards])
    print(unique_ranks)
    if len(unique_ranks) < 5:
        return "Стрита нету"
    else:
        unique_ranks_str = "".join(sorted(unique_ranks, key=lambda card: Card.get_rank_value(card)))
        print(f"Уникальные ранги по возрастанию: {unique_ranks_str}")
        final_ranks = ''
        if (unique_ranks_str[0:4]) == '2345' and ('A' in unique_ranks_str):
            final_ranks = 'A' + unique_ranks_str[:-1]
            print(f"1-ый тест final_ranks: {final_ranks}")
        else:
            final_ranks = unique_ranks_str
            print(f"2-ой тест final_ranks: {final_ranks}")
            # print(final_ranks[2:7])
            # print(final_ranks[1:6])
            # print(final_ranks[0:5])

        if final_ranks[2:7] in straights:
            return 'Вывел стрит после 1-ой проверки', final_ranks[2:7]
        elif final_ranks[1:6] in straights:
            return 'Вывел стрит после 2-ой проверки', final_ranks[1:6]
        elif final_ranks[0:5] in straights:
            return 'Вывел стрит после 3-ей проверки', final_ranks[0:5]
        else:
            return "Стрита нету"


print(is_straight())
