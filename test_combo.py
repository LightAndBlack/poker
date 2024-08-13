from collections import Counter, defaultdict
from card import Card
import time

ROYAL_FLUSH = 1000
STRAIGHT_FLUSH = 900
FOUR_CARDS = 800
FULL_HOUSE = 700
FLUSH = 600
STRAIGHT = 500
THREE_CARDS = 400
TWO_PAIRS = 300
ONE_PAIR = 200
HIGH_CARD = 100


def sort_cards(cards):
    return sorted(cards, key=lambda card: Card.get_card_value(card), reverse=True)


showdown_cards = ['7c', '5c', '6d', '4c', '3c', '2c', 'Ac']
sorted_cards = sort_cards(showdown_cards)


def is_flush(sorted_cards_arg):
    suits_player = [card[-1] for card in sorted_cards_arg]
    has_flush = [k for k, v in Counter(suits_player).items() if v >= 5]

    if has_flush:
        flush_cards = [flush_card for flush_card in sorted_cards_arg if flush_card[1] == has_flush[0]]
        power_flush = FLUSH + Card.get_card_value(flush_cards[0])
        # return "Флэш:", *sorted(flush_cards[0:5], key=lambda card: Card.get_card_value(card), reverse=True), \
        #     "Сила флэша: ", power_flush
        return sorted(flush_cards[0:5], key=lambda card: Card.get_card_value(card))
    else:
        return 0


straights = [
    'A2345', '23456', '34567', '45678', '56789', '6789T',
    '789TJ', '89TJQ', '9TJQK', 'TJQKA'
]


def is_straight(showdown_cards_arg):
    # Создаем словарь, чтобы хранить карты по рангам
    rank_to_cards = defaultdict(list)
    for card in showdown_cards_arg:
        rank = card[:-1]
        rank_to_cards[rank].append(card)
    unique_ranks = set(rank_to_cards.keys())
    if len(unique_ranks) < 5:
        return 0
    else:
        unique_ranks_str = "".join(sorted(unique_ranks, key=lambda cards: Card.get_rank_value(cards)))
        if (unique_ranks_str[0:4]) == '2345' and ('A' in unique_ranks_str):
            final_ranks = 'A' + unique_ranks_str[:-1]
        else:
            final_ranks = unique_ranks_str

        straight_cards = []
        if final_ranks[2:7] in straights:
            power_street = 500 + Card.get_rank_value(final_ranks[6])
            # return 'Cтрит после 1-ой проверки:', final_ranks[2:7], "Сила стрита:", power_street
            for rank in final_ranks[2:7]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards
            # return final_ranks[2:7]
        elif final_ranks[1:6] in straights:
            power_street = 500 + Card.get_rank_value(final_ranks[5])
            # return 'Cтрит после 2-ой проверки:', final_ranks[1:6], "Сила стрита:", power_street
            for rank in final_ranks[1:6]:
                straight_cards.append(rank_to_cards[rank][0])
            # return final_ranks[1:6]
            return straight_cards
        elif final_ranks[0:5] in straights:
            power_street = 500 + Card.get_rank_value(final_ranks[4])
            # return 'Cтрит после 3-ей проверки:', final_ranks[0:5], "Сила стрита:", power_street
            # return final_ranks[0:5]
            for rank in final_ranks[0:5]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards
        else:
            return 0


royal = (
    'AcKcQcJcTc',
    'AdKdQdJdTd',
    'AhKhQhJhTh',
    'AsKsQsJsTs',
)


# royal = (
#     'TcJcQcKcAc',
#     'TdJdQdKdAd',
#     'ThJhQhKhAh',
#     'TsJsQsKsAs',
# )


def is_royal_flush(sorted_cards_arg):
    if "".join(sorted_cards_arg[0:5]) in royal:
        return sorted(sorted_cards_arg[0:5], key=lambda card: Card.get_card_value(card))
    else:
        return 0


def is_straight_flush(showdown_cards_arg):
    if is_straight(showdown_cards_arg) and is_flush(is_straight(showdown_cards_arg)):
        has_straight_flush = is_straight(showdown_cards_arg)
        # print(f"has_straight_flush = {has_straight_flush}")
        power_straight_flush = Card.get_rank_value(has_straight_flush[4][0])
        # return "Стрит-флэш: ", has_straight_flush, "Сила стрит-флэша = ", power_straight_flush
        return has_straight_flush
    else:
        return 0


print(f"Флэш: {is_flush(sorted_cards)}")
print(f"Стрит: {is_straight(showdown_cards)}")
print(f"Роял-флэш: {is_royal_flush(sorted_cards)}")
print(f"Стрит-флэш: {is_straight_flush(sorted_cards)}")
# print(is_straight(showdown_cards))
# print(is_flush(is_straight(showdown_cards)))  # !!!

# Измерение времени выполнения
# start_time = time.perf_counter()
#
# print(f"Роял-флэш: {is_royal_flush(sorted_cards)}")
#
#
# end_time = time.perf_counter()
#
# execution_time_ms = (end_time - start_time) * 1000
# print(f"Execution time: {execution_time_ms:.2f} milliseconds")

# Execution time: 0.05 milliseconds:
#   print(is_flush(sorted_cards))
#   print(is_straight(showdown_cards))

# Execution time: 0.01 milliseconds:
#   1-ая функция определения роял-флэша: ('РОЯЛ ФЛЭШ', ('Cтрит после 3-ей проверки:', 'TJQKA', 'Сила стрита:', 514), 'Сила комбинации: ', 1000)

# Execution time: 0.00 milliseconds
# 2-ая функция определения роял-флэша: ['Ac', 'Kc', 'Qc', 'Jc', 'Tc']
