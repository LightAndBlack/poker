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

num_active_players = 3
players = []
positions = [0, 1, 2]
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

players_to_remove = []
raise_count = 0
players_sort = sorted(players, key=lambda player_arg: players.index(player_arg), reverse=True)
for player in players_sort:
    if player.position == 'BB' and raise_count == 0:
        player.action = float(input(
            f" 0 - fold \n 1 - check \n 2 - call \n 3 - raise \n 4 - all_in\n Игрок {player.name} выберите одно из "
            f"действий выше: "))
    else:
        player.action = float(input(f" 0 - fold\n 2 - call\n 3 - raise\n 4 - all_in\n Игрок {player.name} выберите "
                                    f"одно из действий выше: "))
    match player.action:
        case 0:
            print(f"Игрок {player.name} сбрасывает карты\n")
            players_to_remove.append(player)
            if len(players_sort) - len(players_to_remove) == 1 and raise_count == 0:
                print(f"Игрок {players_sort[0].name} выиграл основной банк")
                break
        case 1 if player.position == "BB":
            print(f"Игрок {player.name} говорит чек и пропускает ход\n")
        case 2:
            print(f"Игрок {player.name} уравнивает ставку\n")
        case 3:
            # print(f"Введите размер ставки от 2 до {player.stack} бб:")
            player.bet = float(input(f"Введите размер ставки от 2 до {player.stack} бб: "))
            print(f"Игрок {player.name} повышает ставку на {player.bet} бб\n")
            raise_count += 1
        case 4:
            print(f"Игрок {player.name} идет all-in\n")
    if player.action == 0:
        pass
        # print(f"Игрок {player.name} выбыл из игры")
        # print(players_sort.index(player))
        # players_sort.remove(player)

for player in players_to_remove:
    players_sort.remove(player)


for player in players_sort:
    print(f"Игрок{player.name} выигрывает основной банк")
    print(player.name, player.stack, player.position)

# TODO условия хода на префлопе - у кого старше индекс позиции, тот ходит первым
# TODO условия хода после префлопа - первый ходит малый блайнд (SB), далее BB и остальные позиции в порядке
# TODO их индексов. КРОМЕ ХЕДЗ-АПА. Там первый ходит ББ!!!
# TODO создать словари для позиции ПРЕФЛОП и ПОСЛЕ ПРЕФЛОПА!!!
