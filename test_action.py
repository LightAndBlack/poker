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

num_active_players = 6
players = []
positions = [0, 1, 2, 3, 4, 5]
round_finished = True


# Инициализация игроков
for i in range(num_active_players):
    buy_in = 100
    player_name = f"Player_{i + 1}"
    player = Player(player_name, stack=buy_in)
    players.append(player)

for player in players:
    print(f"Стек игрока {player.name}: {player.stack} бб")

print("\n")

# Вывод информации об игроках в начале каждой раздачи
for i in range(num_active_players):
    if round_finished:
        positions = [(i + 1) % num_active_players for i in positions]
        print("НОВАЯ РАЗДАЧА: ")
    # Запрашиваем бай-ин у пользователя
    # buy_in = float(input(f"Выберите бай-ин для {player_name} от 40 до 100бб: "))

    # print(f"positions = {positions}")

    for idx, pos in enumerate(positions):
        players[idx].position = POSITION_MAP[pos]

    for player in players:
        if player.position == 'BB':
            player.stack = player.stack - 1
        elif player.position == 'SB':
            player.stack = player.stack - 0.5
        print(f"Стек игрока {player.name}: {player.stack} бб, позиция: {player.position}")
    print("\n")


# TODO условия хода на префлопе - у кого старше индекс позиции, тот ходит первым
# TODO условия хода после префлопа - первый ходит малый блайнд (SB), далее BB и остальные позиции в порядке
# TODO их индексов. КРОМЕ ХЕДЗ-АПА. Там первый ходит ББ!!!
# TODO создать словари для позиции ПРЕФЛОП и ПОСЛЕ ПРЕФЛОПА!!!
