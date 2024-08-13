from collections import Counter
from card import Card
import time


def sort_cards(cards):
    return sorted(cards, key=lambda card: Card.get_card_value(card), reverse=True)


showdown_cards = ['Kh', 'Ac', 'Th', 'Jc', '9h', 'Qh', '8h']
sorted_cards = sort_cards(showdown_cards)


def is_flush(sorted_cards_arg):
    suits_player = [card[-1] for card in sorted_cards_arg]
    has_flush = [k for k, v in Counter(suits_player).items() if v >= 5]

    if has_flush:
        flush_cards = [flush_card for flush_card in sorted_cards_arg if flush_card[1] == has_flush[0]]
        power_flush = 600 + Card.get_card_value(flush_cards[0])
        return "Флэш:", *flush_cards, "Сила флэша: ", power_flush
    else:
        return 0


straights = [
        'A2345', '23456', '34567', '45678', '56789', '6789T',
        '789TJ', '89TJQ', '91TJQK', 'TJQKA'
    ]


def is_straight(showdown_cards_arg):
    unique_ranks = set([rank[0] for rank in showdown_cards_arg])
    if len(unique_ranks) < 5:
        return 0
    else:
        unique_ranks_str = "".join(sorted(unique_ranks, key=lambda card: Card.get_rank_value(card)))
        if (unique_ranks_str[0:4]) == '2345' and ('A' in unique_ranks_str):
            final_ranks = 'A' + unique_ranks_str[:-1]
        else:
            final_ranks = unique_ranks_str

        if final_ranks[2:7] in straights:
            power_street = 500 + Card.get_rank_value(final_ranks[6])
            return 'Cтрит после 1-ой проверки:', final_ranks[2:7], "Сила стрита:", power_street
        elif final_ranks[1:6] in straights:
            power_street = 500 + Card.get_rank_value(final_ranks[5])
            return 'Cтрит после 2-ой проверки:', final_ranks[1:6], "Сила стрита:", power_street
        elif final_ranks[0:5] in straights:
            power_street = 500 + Card.get_rank_value(final_ranks[4])
            return 'Cтрит после 3-ей проверки:', final_ranks[0:5], "Сила стрита:", power_street
        else:
            return 0


# Измерение времени выполнения
start_time = time.perf_counter()

print(is_flush(sorted_cards))
print(is_straight(showdown_cards))


end_time = time.perf_counter()

execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.2f} milliseconds")

# Execution time: 0.05 milliseconds
