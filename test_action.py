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
            player.share = 1
        elif player.position == 'SB':
            player.stack = player.stack - 0.5
            player.share = 0.5
        else:
            player.share = 0
        print(f"Стек игрока {player.name}: {player.stack} бб, позиция: {player.position}")
    print("\n")

players_to_remove = []


def preflop_action():
    players_sort = sorted(players, key=lambda player_arg: players.index(player_arg), reverse=True)
    count_players = len(players_sort)
    raise_count = 0
    call_count = 0
    fold_count = 0
    pot = 1.5
    last_bet = 1
    players_raise = []
    call_players = []
    flag = True
    while flag:
        for player in players_sort:
            # print(f"player_position для игрока {player.name} = {player.position}, player.share = {player.share}")
            if player.position == 'BB' and not players_raise:
                player.action = float(input(
                    f" 0 - fold \n 1 - check \n 2 - call \n 3 - raise \n 4 - all_in\n \n pot = {pot} бб\n Игрок {player.name} выберите одно из "
                    f"действий выше: "))
                if raise_count == 0 and player.action == 1:
                    call_players.append(player)
                    print("ПЕРЕХОДИМ КО ФЛОПУ: ")
                    for cpl in call_players:
                        print(f"count_players = {cpl.name}, position = {cpl.position}")
                    flag = False
                elif raise_count == 0 and player.action == 0:
                    fold_count += 1
                    flag = False
            else:
                player.action = float(input(
                    f" 0 - fold\n 2 - call\n 3 - raise\n 4 - all_in\n \n pot = {pot} бб\n Игрок {player.name} выберите "
                    f"одно из действий выше: "))
            # print(f"pot = {pot} бб\n")
            # if call_players:
            #     for cpl in call_players:
            #         print(f"call_players = {cpl}")
            match player.action:
                case 0:
                    fold_count += 1
                    print(f"Игрок {player.name} сбрасывает карты\n")
                    players_to_remove.append(player)
                    for player_removed in players_to_remove:
                        print(f"player_removed = {player_removed.name}")
                        print(f"count_of_removed_players = {len(players_to_remove)}")
                        print(f"players_sort[0].name = {players_sort[0].name}")
                        print()
                    if len(players_sort) - len(players_to_remove) == 1 and raise_count == 0:
                        print(f"Игрок {players_sort[-1].name} выиграл основной банк")
                        flag = False
                    # elif len(players_sort) - fold_count == 1 and players_raise:
                    elif players_raise and fold_count + raise_count + call_count == count_players:
                        if fold_count == count_players - 1:
                            print(f"Игрок {players_raise[0].name} выиграл основной банк")
                            flag = False
                            break
                        else:
                            print("ПЕРЕХОДИМ КО ФЛОПУ: ")
                            for cpl in call_players:
                                print(f"count_players = {cpl.name}, position = {cpl.position}")
                            flag = False
                            break
                    elif players_raise and fold_count == count_players - 1:
                        print(f"Игрок {players_raise[0].name} выиграл основной банк")
                        flag = False
                        break
                    print(f"fold_count = {fold_count}")
                    print(f"call_count = {call_count}")
                    print(f"raise_count = {raise_count}")
                    # elif players_raise and fold_count + raise_count == call_count:
                    #     print("ПЕРЕХОДИМ КО ФЛОПУ: ")
                    #     flag = False
                    # if players_raise and fold_count + raise_count + call_count == count_players:
                    #     print("ПЕРЕХОДИМ КО ФЛОПУ: ")
                    #     flag = False
                case 1 if player.position == "BB":
                    # print(f"\n pot = {pot} бб")
                    print(f"Игрок {player.name} говорит чек и пропускает ход\n")
                case 2:
                    print(f"Игрок {player.name} уравнивает ставку\n")
                    call_count += 1
                    dif_to_call = last_bet - player.share
                    player.share = dif_to_call
                    pot += dif_to_call
                    player.stack -= dif_to_call
                    print(f"player.stack = {player.stack}")
                    print(f"\n pot = {pot} бб, {player.name} stack = {player.stack}")
                    call_players.append(player)
                    if call_players:
                        for cpl in call_players:
                            print(f"call_players = {cpl}")
                    print(f"fold_count = {fold_count}")
                    print(f"call_count = {call_count}")
                    print(f"raise_count = {raise_count}")
                    if players_raise and fold_count + raise_count + call_count == count_players:
                        print("ПЕРЕХОДИМ КО ФЛОПУ: ")
                        for cpl in call_players:
                            print(f"count_players = {cpl.name}, position = {cpl.position}")
                        flag = False
                        break
                    # print(f"next(iter(call_players) = {next(iter(call_players))}")
                    # if players_raise and next(iter(call_players)) == players_raise[0]:
                    #     print(f"next(iter(call_players) = {next(iter(call_players))}")
                    #     flag = False
                    # players_raise.clear()
                case 3:
                    # print(f"\npot = {pot} бб")
                    player.bet = float(input(f"Введите размер ставки от 2 до {player.stack} бб: "))
                    last_bet = player.bet
                    pot += last_bet
                    print(f"\npot = {pot} бб")
                    print(f"Игрок {player.name} повышает ставку на {last_bet} бб\n")
                    raise_count = 1
                    call_count = 0
                    # players_raise.append(player)
                    if raise_count:
                        # call_players.clear()
                        # call_count = 0
                        players_raise.clear()
                    call_players.append(player)
                    players_raise.append(player)
                    for cpl in call_players:
                        print(f"call_players = {cpl}")
                    print(f"fold_count = {fold_count}")
                    print(f"call_count = {call_count}")
                    print(f"raise_count = {raise_count}")
                case 4:
                    # print(f"\n pot = {pot} бб")
                    print(f"Игрок {player.name} идет all-in\n")
            # if len(players_sort) - fold_count == 1 and raise_count == 0:
            #     print(f"Игрок {players_sort[-1].name} выиграл основной банк")
            #     break
            # elif len(players_sort) - fold_count == 1 and players_raise:
            #     print(f"Игрок {players_raise[0].name} выиграл основной банк")
            #     break

            if not flag:
                break


# for player in players_to_remove:
#     players_sort.remove(player)
#
# if len(players_sort) - len(players_to_remove) == 1 and raise_count == 0:
#     print(f"Игрок {players_sort[0].name} выиграл основной банк")
# for player in players_sort:
#     print(f"Игрок{player.name} выигрывает основной банк")
#     print(player.name, player.stack, player.position)


preflop_action()
print("ФЛОП: \n")

# position

# TODO условия хода на префлопе - у кого старше индекс позиции, тот ходит первым
# TODO условия хода после префлопа - первый ходит малый блайнд (SB), далее BB и остальные позиции в порядке
# TODO их индексов. КРОМЕ ХЕДЗ-АПА. Там первый ходит ББ!!!
# TODO создать словари для позиции ПРЕФЛОП и ПОСЛЕ ПРЕФЛОПА!!!
