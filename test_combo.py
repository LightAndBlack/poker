from collections import Counter
from card import Card


# sorted(iterable,key=None,reverse=False)
def sort_cards(cards):
    return sorted(cards, key=lambda card: Card.get_card_value(card), reverse=True)


showdown_cards = ['Ah', 'Kc', '5d', '7c', '4h', '3h', '2h']
sorted_cards = sort_cards(showdown_cards)  # начальная сортировка карт по рангу
print(sorted_cards)


# Определяю флэш
def is_flush(sorted_cards_arg):
    suits_player = [card[-1] for card in sorted_cards_arg]
    print(suits_player)
    has_flush = [k for k, v in Counter(suits_player).items() if v >= 5]

    if has_flush:
        flush_cards = [flush_card for flush_card in sorted_cards_arg if flush_card[1] == has_flush[0]]
        power_flush = 800 + Card.get_card_value(flush_cards[0])
        return "Флэш", flush_cards, power_flush
    else:
        return 0


# Определяю стрит
straights = [
        'A2345', '23456', '34567', '45678', '56789', '678910',
        '78910J', '8910JQ', '910JQK', '10JQKA'
    ]


def is_straight(showdown_cards_arg):
    unique_ranks = set([rank[0] for rank in showdown_cards_arg])
    print(unique_ranks)
    if len(unique_ranks) < 5:
        return 0
    else:
        unique_ranks_str = "".join(sorted(unique_ranks, key=lambda card: Card.get_rank_value(card)))
        print(f"Уникальные ранги по возрастанию: {unique_ranks_str}")
        if (unique_ranks_str[0:4]) == '2345' and ('A' in unique_ranks_str):
            final_ranks = 'A' + unique_ranks_str[:-1]
            print(f"1-ый тест final_ranks: {final_ranks}")
        else:
            final_ranks = unique_ranks_str
            print(f"2-ой тест final_ranks: {final_ranks}")

        if final_ranks[2:7] in straights:
            return 'Вывел стрит после 1-ой проверки', final_ranks[2:7]
        elif final_ranks[1:6] in straights:
            return 'Вывел стрит после 2-ой проверки', final_ranks[1:6]
        elif final_ranks[0:5] in straights:
            return 'Вывел стрит после 3-ей проверки', final_ranks[0:5]
        else:
            return 0


print(is_flush(sorted_cards))
print(is_straight(showdown_cards))
