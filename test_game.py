import random

from deck import Deck
from player import Player

current_deck = Deck.get_deck()
random.shuffle(current_deck)
print(*current_deck, f" Всего {len(current_deck)} карт")


def start_hand():
    hand = [current_deck.pop(0), current_deck.pop(0)]
    current_deck.pop(0)
    return hand


num_active_players = 6

players = {}

# Создание и добавление игроков в словарь
for i in range(num_active_players):
    player_name = f"Player {i + 1}"
    players[player_name] = Player(player_name, start_hand())


# Функция для получения карт всех игроков
def get_all_player_hands(players_dict):
    """
    Возвращает словарь, где ключи — имена игроков, а значения — строки с их картами.

    :param players_dict: Словарь игроков, где ключ — имя игрока, значение — объект Player.
    :return: Словарь, где ключи — имена игроков, а значения — строки с картами.
    """
    result = {}
    for player_name_local, player_obj in players_dict.items():
        result[player_name_local] = ', '.join(player_obj.pocket_hand)
    return result


all_start_hands = get_all_player_hands(players)
print(all_start_hands)
print(all_start_hands['Player 1'], type(all_start_hands['Player 1']))


def get_flop():
    local_flop = [current_deck.pop(0), current_deck.pop(0), current_deck.pop(0)]
    current_deck.pop(0)
    return local_flop


flop = get_flop()
print(f"FLOP: {', '.join(flop)}")


def get_turn():
    flop.append(current_deck.pop(0))
    current_deck.pop(0)
    return flop


turn = get_turn()
print(f"TURN: {', '.join(turn)}")


def get_river():
    flop.append(current_deck.pop(0))
    current_deck.pop(0)
    return flop


river = get_river()
print(f"RIVER: {', '.join(river)}")
print(*current_deck, f" Всего {len(current_deck)} карт")
