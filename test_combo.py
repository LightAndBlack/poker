from collections import Counter, defaultdict
from card import Card
from test_game import players, river
from player import Player


def get_combined_hands(players_dict, river_cards):
    combined_hands = {}
    for player_name, player in players_dict.items():
        combined_hand = player.pocket_hand + river_cards
        combined_hands[player_name] = combined_hand
    return combined_hands


all_hands = get_combined_hands(players, river)
# print(all_hands)

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


showdown_cards = ['8s', 'Td', '9s', '9d', 'Ts', '8h', 'Th']
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
        return sorted(flush_cards, key=lambda card: Card.get_card_value(card)), power_flush
    else:
        return 0


def is_straight(showdown_cards_arg):
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
            for rank in final_ranks[2:7]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards, power_street
        elif final_ranks[1:6] in straights:
            power_street = STRAIGHT + Card.get_rank_value(final_ranks[5])
            for rank in final_ranks[1:6]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards, power_street
        elif final_ranks[0:5] in straights:
            power_street = STRAIGHT + Card.get_rank_value(final_ranks[4])
            for rank in final_ranks[0:5]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards, power_street
        else:
            return 0


def is_straight_flush(showdown_cards_arg):
    flush_result = is_flush(showdown_cards_arg)
    if flush_result == 0:
        return 0
    else:
        flush_cards = flush_result[0]
        rank_to_cards = defaultdict(list)
    for card in flush_cards:
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
            for rank in final_ranks[2:7]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards, power_street
        elif final_ranks[1:6] in straights:
            power_street = STRAIGHT_FLUSH + Card.get_rank_value(final_ranks[5])
            for rank in final_ranks[1:6]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards, power_street
        elif final_ranks[0:5] in straights:
            power_street = STRAIGHT_FLUSH + Card.get_rank_value(final_ranks[4])
            for rank in final_ranks[0:5]:
                straight_cards.append(rank_to_cards[rank][0])
            return straight_cards, power_street
        else:
            return 0


# all_showdown_combos = [v for k, v in all_hands.items()]
# print(all_showdown_combos)
#
# for combo in all_showdown_combos:
#     has_match = Counter([card[0] for card in sort_cards(combo)])  # !!!!!!
#     has_quads = [k for k, v in has_match.items() if v == 4]
#     has_set = [k for k, v in has_match.items() if v == 3]
#     has_pair = [k for k, v in has_match.items() if v == 2]


# has_match = Counter([card[0] for card in sort_cards(all_hands['Player 1'])])  # !!!!!!
# has_quads = [k for k, v in has_match.items() if v == 4]
# has_set = [k for k, v in has_match.items() if v == 3]
# has_pair = [k for k, v in has_match.items() if v == 2]


# has_match = Counter([card[0] for card in sort_cards(sorted_cards)])
# has_quads = [k for k, v in has_match.items() if v == 4]
# has_set = [k for k, v in has_match.items() if v == 3]
# has_pair = [k for k, v in has_match.items() if v == 2]


def is_quads(sorted_cards_arg):
    has_match = Counter([card[0] for card in sort_cards(sorted_cards_arg)])
    has_quads = [k for k, v in has_match.items() if v == 4]
    if has_quads:
        quads = [card for card in sorted_cards_arg if card[0] == has_quads[0]]
        if has_quads[0] == sorted_cards_arg[0][0]:
            quads.append(sorted_cards_arg[4])
            power_combo = FOUR_CARDS + Card.get_card_value(quads[4]) + Card.get_card_value(quads[0]) * 4
        else:
            quads.insert(0, sorted_cards_arg[0])
            power_combo = FOUR_CARDS + Card.get_card_value(quads[0]) + Card.get_card_value(quads[4]) * 4
        return quads, power_combo
    else:
        return 0


def is_full_house(sorted_cards_arg):
    has_match = Counter([card[0] for card in sort_cards(sorted_cards_arg)])
    has_set = [k for k, v in has_match.items() if v == 3]
    has_pair = [k for k, v in has_match.items() if v == 2]
    if has_set and has_pair:
        three_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_set[0]]
        two_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_pair[0]]
        power_combo = FULL_HOUSE + Card.get_rank_value(has_set[0]) * 3 + Card.get_rank_value(has_pair[0]) * 2/100
        return three_equal_ranks + two_equal_ranks, power_combo
    elif has_set and len(has_set) == 2:
        three_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_set[0]]
        two_equal_ranks = [card for card in sorted_cards_arg if card[0] == has_set[1]]
        power_combo = FULL_HOUSE + Card.get_rank_value(has_set[0]) * 3 + Card.get_rank_value(has_set[1]) * 2/100
        return three_equal_ranks + two_equal_ranks[:-1], power_combo
    else:
        return 0


def is_set(sorted_cards_arg):
    has_match = Counter([card[0] for card in sort_cards(sorted_cards_arg)])
    has_set = [k for k, v in has_match.items() if v == 3]
    if has_set:
        set_combo = [card for card in sorted_cards_arg if card[0] == has_set[0]]
        if set_combo[0][0] == sorted_cards_arg[0][0]:
            set_combo.extend(sorted_cards_arg[3:5])
        elif set_combo[0][0] == sorted_cards_arg[1][0]:
            set_combo.append(sorted_cards_arg[0])
            set_combo.append(sorted_cards_arg[4])
        else:
            set_combo.append(sorted_cards_arg[1])
            set_combo.append(sorted_cards_arg[0])
        ranks_combo = sum([Card.get_card_value(rank) for rank in set_combo])
        power_combo = SET + ranks_combo
        return set_combo, power_combo
    else:
        return 0


def is_two_pairs(sorted_cards_arg):
    has_match = Counter([card[0] for card in sort_cards(sorted_cards_arg)])
    has_pair = [k for k, v in has_match.items() if v == 2]
    if len(has_pair) >= 2:
        first_pair = [card for card in sorted_cards_arg if card[0] == has_pair[0]]
        second_pair = [card for card in sorted_cards_arg if card[0] == has_pair[1]]
        two_pairs = first_pair + second_pair
        if Card.get_card_value(sorted_cards_arg[0]) > Card.get_card_value(first_pair[0]):
            two_pairs.append(sorted_cards_arg[0])
        elif Card.get_card_value(first_pair[0]) > Card.get_card_value(sorted_cards_arg[2]) > Card.get_card_value(
                second_pair[0]):
            two_pairs.append(sorted_cards_arg[2])
        else:
            two_pairs.append(sorted_cards_arg[4])
        sum_ranks_combo = sum([Card.get_card_value(card) for card in two_pairs])
        power_combo = TWO_PAIRS + sum_ranks_combo
        return two_pairs, power_combo
    else:
        return 0


def is_one_pair(sorted_cards_arg):
    has_match = Counter([card[0] for card in sort_cards(sorted_cards_arg)])
    has_pair = [k for k, v in has_match.items() if v == 2]
    if has_pair:
        one_pair = [card for card in sorted_cards_arg if card[0] == has_pair[0]]
        first_index = sorted_cards_arg.index(one_pair[0])
        remaining_cards = sorted_cards_arg[0:first_index] + sorted_cards_arg[first_index + 2:]
        one_pair_combo = one_pair + remaining_cards[:3]
        sum_ranks_combo = sum([Card.get_card_value(card) for card in one_pair_combo])
        power_combo = ONE_PAIR + sum_ranks_combo
        return one_pair_combo, power_combo
    else:
        return 0


def evaluate_combo(sorted_cards_args):
    if is_royal_flush(sorted_cards_args):
        return "Роял-флэш    ", *is_royal_flush(sorted_cards_args), ROYAL_FLUSH
    elif is_straight_flush(sorted_cards_args):
        return "Стрит-флэш   ", is_straight_flush(sorted_cards_args)
    elif is_quads(sorted_cards_args):
        return "Каре         ", is_quads(sorted_cards_args)
    elif is_full_house(sorted_cards_args):
        return "Фул-хаус     ", is_full_house(sorted_cards_args)
    elif is_flush(sorted_cards_args):
        flush = is_flush(sorted_cards_args)
        return "Флэш         ", flush[-5:]
    elif is_straight(sorted_cards_args):
        return "Стрит        ", is_straight(sorted_cards_args)
    elif is_set(sorted_cards_args):
        return "Сет          ", is_set(sorted_cards_args)
    elif is_two_pairs(sorted_cards_args):
        return "Две пары     ", is_two_pairs(sorted_cards_args)
    elif is_one_pair(sorted_cards_args):
        return "Пара         ", is_one_pair(sorted_cards_args)
    else:
        sum_ranks_combo = sum([Card.get_card_value(card) for card in sorted_cards_args[:5]])
        power_combo = HIGH_CARD + sum_ranks_combo
        return "Старшая карта", (sorted_cards_args[:5], power_combo)


print(evaluate_combo(sorted_cards))

# for start_hand in players.values():


# print(all_hands['Player 1'])
# print(sort_cards(all_hands['Player 1']))
# player1 = sort_cards(all_hands['Player 1'])
# print(player1, type(player1))
# print(evaluate_combo(player1))

# all_showdown_combos = [v for k, v in all_hands.items()]
# # print(all_showdown_combos)
# #
# for combo in all_showdown_combos:
#     print(evaluate_combo(sort_cards(combo)))

for players, hand in all_hands.items():
    print(f"{players}: {evaluate_combo(sort_cards(hand))}")
