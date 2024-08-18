from typing import Dict

from stack_player import Player

POSITION_MAP = {
    'BB': 1,
    'SB': 2,
    'BTN': 3,
    'CO': 4,
    'MP': 5,
    'UTG': 6
}

BOARD_MAP = {
    'SB': 1,
    'BB': 2,
    'UTG': 3,
    'MP': 4,
    'CO': 5,
    'BTN': 6
}

positions = ['BB', 'SB', 'BTN', 'CO', 'MP', 'UTG']

num_active_players = 6
players = []

for i in range(num_active_players):
    player_name = f"Player_{i + 1}"

    # Запрашиваем бай-ин у пользователя
    # buy_in = float(input(f"Выберите бай-ин для {player_name} от 40 до 100бб: "))
    buy_in = 100
    position = positions[i % len(positions)]

    player = Player(player_name, stack=buy_in, position=position)

    players.append(player)


# Вывод информации о всех игроках
for player in players:
    if player.position == 'BB':
        player.stack = player.stack - 1
    elif player.position == 'SB':
        player.stack = player.stack - 0.5
    print(f"Стек игрока {player.name}: {player.stack} бб, позиция: {player.position}")

total_positions = num_active_players
print(f"total_positions = {total_positions}")


# Смена позиций после раунда
def rotate_positions(players_arg, positions_arg):
    # Сдвиг позиций на 1 вперед
    positions_arg = positions_arg[-1:] + positions_arg[:-1]
    # Обновление позиций у игроков
    for idx, player_arg in enumerate(players):
        player_arg.position = positions[idx % len(positions)]
    return positions


# Пример смены позиций после раунда
positions = rotate_positions(players, positions)

print("\nПосле смены позиций:")
# players = rotate_positions(players)
# for player in players:
#     print(player)


# TODO условия хода на префлопе - у кого старше индекс позиции, тот ходит первым
# TODO условия хода после префлопа - первый ходит малый блайнд (SB), далее BB и остальные позиции в порядке
# TODO их индексов. КРОМЕ ХЕДЗ-АПА. Там первый ходит ББ!!!
# TODO создать словари для позиции ПРЕФЛОП и ПОСЛЕ ПРЕФЛОПА!!!

