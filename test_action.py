from typing import Dict

from stack_player import Player

POSITION_MAP = {
    0: 'BB',
    1: 'SB',
    2: 'BTN',
    3: 'CO',
    4: 'MP',
    5: 'UTG'
}

BOARD_MAP = {
    'SB': 1,
    'BB': 2,
    'UTG': 3,
    'MP': 4,
    'CO': 5,
    'BTN': 6
}

# positions = ['BB', 'SB', 'BTN', 'CO', 'MP', 'UTG']
positions = [0, 1, 2, 3, 4, 5]
round_finished = False

num_active_players = 6
players = []

for i in range(num_active_players):
    player_name = f"Player_{i + 1}"

    # Запрашиваем бай-ин у пользователя
    # buy_in = float(input(f"Выберите бай-ин для {player_name} от 40 до 100бб: "))
    buy_in = 100
    # position = positions[i % len(positions)]
    position = positions[i]

    player = Player(player_name, stack=buy_in, position=POSITION_MAP[position])

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


for i in range(num_active_players):

    round_finished = True
    print("НОВАЯ РАЗДАЧА: ")

    if round_finished:
        positions = [(i + 1) % num_active_players for i in positions]

    print(positions, "\n")



# TODO условия хода на префлопе - у кого старше индекс позиции, тот ходит первым
# TODO условия хода после префлопа - первый ходит малый блайнд (SB), далее BB и остальные позиции в порядке
# TODO их индексов. КРОМЕ ХЕДЗ-АПА. Там первый ходит ББ!!!
# TODO создать словари для позиции ПРЕФЛОП и ПОСЛЕ ПРЕФЛОПА!!!

