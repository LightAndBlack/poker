from collections import Counter, defaultdict
from card import Card
import time

ROYAL_FLUSH = 1000
STRAIGHT_FLUSH = 900
FOUR_CARDS = 800
FULL_HOUSE = 700
FLUSH = 600
STRAIGHT = 500
SET = 400
TWO_PAIRS = 300
ONE_PAIR = 200
HIGH_CARD = 100


def sort_cards(cards):
    return sorted(cards, key=lambda card: Card.get_card_value(card), reverse=True)


showdown_cards = ['Th', '5s', '9c', '9d', '5c', 'Qd', 'Js']
sorted_cards = sort_cards(showdown_cards)

royal = (
    'AcKcQcJcTc',
    'AdKdQdJdTd',
    'AhKhQhJhTh',
    'AsKsQsJsTs',
)

straights = [
    'A2345', '23456', '34567', '45678', '56789', '6789T',
    '789TJ', '89TJQ', '9TJQK', 'TJQKA'
]


def is_royal_flush(sorted_cards_arg):
    if "".join(sorted_cards_arg[0:5]) in royal:
        return sorted(sorted_cards_arg[0:5], key=lambda card: Card.get_card_value(card))
    else:
        return 0


def is_flush(sorted_cards_arg):
    suits_player = [card[-1] for card in sorted_cards_arg]
    has_flush = [k for k, v in Counter(suits_player).items() if v >= 5]

    if has_flush:
        flush_cards = [flush_card for flush_card in sorted_cards_arg if flush_card[1] == has_flush[0]]
        power_flush = FLUSH + Card.get_card_value(flush_cards[0])
        # return "Флэш:", *sorted(flush_cards[0:5], key=lambda card: Card.get_card_value(card), reverse=True), \
        #     "Сила флэша: ", power_flush
        # return sorted(flush_cards[0:5], key=lambda card: Card.get_card_value(card))
        # print(f"power_flush = {power_flush}")
        return sorted(flush_cards, key=lambda card: Card.get_card_value(card))
    else:
        return 0


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
            straight_wheel = []
            for rank in final_ranks[0:5]:
                straight_wheel.append(rank_to_cards[rank][0])
        else:
            final_ranks = unique_ranks_str

        straight_cards = []
        if final_ranks[2:7] in straights:
            power_street = STRAIGHT + Card.get_rank_value(final_ranks[6])
            # return 'Cтрит после 1-ой проверки:', final_ranks[2:7], "Сила стрита:", power_street
            for rank in final_ranks[2:7]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards
            # return final_ranks[2:7]
        elif final_ranks[1:6] in straights:
            power_street = STRAIGHT + Card.get_rank_value(final_ranks[5])
            # return 'Cтрит после 2-ой проверки:', final_ranks[1:6], "Сила стрита:", power_street
            for rank in final_ranks[1:6]:
                straight_cards.append(rank_to_cards[rank][0])
            # return final_ranks[1:6]
            return straight_cards
        elif final_ranks[0:5] in straights:
            power_street = STRAIGHT + Card.get_rank_value(final_ranks[4])
            # return 'Cтрит после 3-ей проверки:', final_ranks[0:5], "Сила стрита:", power_street
            # return final_ranks[0:5]
            for rank in final_ranks[0:5]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards
        else:
            return 0


# print(f"is_flush(sorted_cards) = {is_flush(sorted_cards)}")
# print(f"is_straight(showdown_cards) = {is_straight(showdown_cards)}")


def is_straight_flush(showdown_cards_arg):
    # Создаем словарь, чтобы хранить карты по рангам
    if not is_flush(showdown_cards_arg):
        return 0
    else:
        rank_to_cards = defaultdict(list)
    for card in is_flush(showdown_cards_arg):
        rank = card[:-1]
        rank_to_cards[rank].append(card)
    unique_ranks = set(rank_to_cards.keys())
    if len(unique_ranks) < 5:
        return 0
    else:
        unique_ranks_str = "".join(sorted(unique_ranks, key=lambda cards: Card.get_rank_value(cards)))
        if (unique_ranks_str[0:4]) == '2345' and ('A' in unique_ranks_str):
            final_ranks = 'A' + unique_ranks_str[:-1]
            straight_wheel = []
            for rank in final_ranks[0:5]:
                straight_wheel.append(rank_to_cards[rank][0])
        else:
            final_ranks = unique_ranks_str

        straight_cards = []
        if final_ranks[2:7] in straights:
            power_street = STRAIGHT_FLUSH + Card.get_rank_value(final_ranks[6])
            # return 'Cтрит после 1-ой проверки:', final_ranks[2:7], "Сила стрита:", power_street
            for rank in final_ranks[2:7]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards
            # return final_ranks[2:7]
        elif final_ranks[1:6] in straights:
            power_street = STRAIGHT_FLUSH + Card.get_rank_value(final_ranks[5])
            # return 'Cтрит после 2-ой проверки:', final_ranks[1:6], "Сила стрита:", power_street
            for rank in final_ranks[1:6]:
                straight_cards.append(rank_to_cards[rank][0])
            # return final_ranks[1:6]
            return straight_cards
        elif final_ranks[0:5] in straights:
            power_street = STRAIGHT_FLUSH + Card.get_rank_value(final_ranks[4])
            # return 'Cтрит после 3-ей проверки:', final_ranks[0:5], "Сила стрита:", power_street
            # return final_ranks[0:5]
            for rank in final_ranks[0:5]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards
        else:
            return 0


# print(f"Стрит-флэш: {is_straight_flush(sorted_cards)}")
# def is_four_ranks():
#     pass

# ranks_lst = []
has_match = Counter([card[0] for card in sorted_cards])
# print(has_match)
# keys = has_match.keys()
# values = has_match.values()
# print("Ключи:", keys)
# print("Значения:", values)
has_quads = [k for k, v in has_match.items() if v == 4]
has_set = [k for k, v in has_match.items() if v == 3]
has_pair = [k for k, v in has_match.items() if v == 2]
# print(f"Каре по {has_quads}")
# print(f"Сет по {has_set}")
# print(f"Пара {has_pair}")


# print(sorted_cards)


def is_quads(sorted_cards_arg):
    if has_quads:
        quads = [card for card in sorted_cards_arg if card[0] == has_quads[0]]
        if has_quads[0] == sorted_cards_arg[0][0]:
            quads.append(sorted_cards_arg[4])
            power_combo = FOUR_CARDS + Card.get_card_value(quads[4]) + Card.get_card_value(quads[0]) * 4
            # print(power_combo)
        else:
            quads.insert(0, sorted_cards_arg[0])
            power_combo = FOUR_CARDS + Card.get_card_value(quads[0]) + Card.get_card_value(quads[4]) * 4
            # print(power_combo)
        return quads
    else:
        return 0

# three_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_set[0]]
# two_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_pair[0]]


def is_full_house(sorted_cards_arg):
    if has_set and has_pair:
        three_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_set[0]]
        # print(f"three_equal_ranks = {three_equal_ranks}")
        two_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_pair[0]]
        # print(f"two_equal_ranks = {two_equal_ranks}")
        power_combo = FULL_HOUSE + Card.get_rank_value(has_set[0]) * 3 + Card.get_rank_value(has_pair[0]) * 2
        print(power_combo)
        return three_equal_ranks + two_equal_ranks
    elif has_set and len(has_set) == 2:
        three_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_set[0]]
        two_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_set[1]]
        power_combo = FULL_HOUSE + Card.get_rank_value(has_set[0]) * 3 + Card.get_rank_value(has_set[1]) * 2
        print(power_combo)
        return three_equal_ranks + two_equal_ranks[:-1]
    else:
        return 0


def is_set(sorted_cards_arg):
    if has_set:
        set_combo = [card for card in sorted_cards_arg if card[0] == has_set[0]]
        # print(f"set_combo[0[0] = {set_combo[0][0]}")
        # print(f"sorted_cards_arg[0][0] = {sorted_cards_arg[0][0]}")
        # print(f"sorted_cards_arg = {sorted_cards_arg}")
        if set_combo[0][0] == sorted_cards_arg[0][0]:
            set_combo.extend(sorted_cards_arg[3:5])
        elif set_combo[0][0] == sorted_cards_arg[1][0]:
            set_combo.append(sorted_cards_arg[0])
            set_combo.append(sorted_cards_arg[4])
        else:
            # print(sorted_cards_arg[0:2])
            # print(sorted_cards_arg[0:2].extend(set_combo))
            # set_combo.insert(0, sorted_cards_arg[0])
            # set_combo.insert(1, sorted_cards_arg[1])
            set_combo.append(sorted_cards_arg[1])
            set_combo.append(sorted_cards_arg[0])
        ranks_combo = sum([Card.get_card_value(rank) for rank in set_combo])
        # print(ranks_combo)
        power_combo = SET + ranks_combo
        # print(power_combo)
        return set_combo
    else:
        return 0


def is_two_pairs(sorted_cards_arg):
    if len(has_pair) == 2:
        first_pair = [card for card in sorted_cards_arg if card[0] == has_pair[0]]
        second_pair = [card for card in sorted_cards_arg if card[0] == has_pair[1]]
        # print(first_pair[0])
        # print(sorted_cards_arg[0])
        two_pairs = second_pair + first_pair
        # print(Card.get_card_value(sorted_cards_arg[0]))
        # print(Card.get_card_value(first_pair[0]))
        if Card.get_card_value(sorted_cards_arg[0]) > Card.get_card_value(first_pair[0]):
            two_pairs.append(sorted_cards_arg[0])
        elif Card.get_card_value(first_pair[0]) > Card.get_card_value(sorted_cards_arg[2]) > Card.get_card_value(second_pair[0]):
            two_pairs.append(sorted_cards_arg[2])
        else:
            two_pairs.append(sorted_cards_arg[4])
        ranks_combo = sum([Card.get_card_value(card) for card in two_pairs])
        # print(ranks_combo)
        return two_pairs
    else:
        return 0


# print(is_two_pairs(sorted_cards))
# print(is_quads(sorted_cards))
# print(is_full_house(sorted_cards))
# print(is_set(sorted_cards))


def evaluate_combo():
    if is_royal_flush(sorted_cards):
        return "Роял-флэш", *is_royal_flush(sorted_cards)
    elif is_straight_flush(showdown_cards):
        return "Стрит-флэш", is_straight_flush(showdown_cards)
    elif is_quads(sorted_cards):
        return "Каре: ", is_quads(sorted_cards)
    elif is_full_house(sorted_cards):
        return "Фул-хаус: ", is_full_house(sorted_cards)
    elif is_flush(sorted_cards):
        return "Флэш", is_flush(sorted_cards)
    elif is_straight(showdown_cards):
        return "Стрит", is_straight(showdown_cards)
    elif is_set(sorted_cards):
        return "Сет", is_set(sorted_cards)
    elif is_two_pairs(sorted_cards):
        return "Две пары", is_two_pairs(sorted_cards)
    else:
        return "Старшая карта"


print(evaluate_combo())

# Измерение времени выполнения
# start_time = time.perf_counter()
# #
# print(f"Флэш: {is_flush(sorted_cards)}")
# print(f"Стрит: {is_straight(showdown_cards)}")
# #
# #
# end_time = time.perf_counter()
# #
# execution_time_ms = (end_time - start_time) * 1000
# print(f"Execution time: {execution_time_ms:.2f} milliseconds")

# Execution time: 0.05 milliseconds:
#   print(is_flush(sorted_cards))
#   print(is_straight(showdown_cards))

# Execution time: 0.01 milliseconds:
#   1-ая функция определения роял-флэша: ('РОЯЛ ФЛЭШ', ('Cтрит после 3-ей проверки:', 'TJQKA', 'Сила стрита:', 514), 'Сила комбинации: ', 1000)

# Execution time: 0.00 milliseconds
# 2-ая функция определения роял-флэша: ['Ac', 'Kc', 'Qc', 'Jc', 'Tc']
