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
    'SB': 0,
    'BB': 1,
    'UTG': 2,
    'MP': 3,
    'CO': 4,
    'BTN': 5
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
                    f"Игрок {player.name} выберите действие (0 - fold, 1 - check, 2 - call, 3 - raise, 4 - all_in): "))
                if raise_count == 0 and player.action == 1:
                    call_players.append(player)
                    print("\nПЕРЕХОДИМ КО ФЛОПУ: ")
                    for cpl in call_players:
                        print(f"count_players = {cpl.name}, position = {cpl.position}")
                    return call_players, pot
                    # flag = False
                elif raise_count == 0 and player.action == 0:
                    fold_count += 1
                    flag = False
            else:
                player.action = float(input(
                    f"Игрок {player.name} выберите действие (0 - fold, 2 - call, 3 - raise, 4 - all_in): "))
            # print(f"pot = {pot} бб\n")
            # if call_players:
            #     for cpl in call_players:
            #         print(f"call_players = {cpl}")
            match player.action:
                case 0:
                    fold_count += 1
                    print(f"Игрок {player.name} сбрасывает карты\n")
                    players_to_remove.append(player)
                    if player in call_players:
                        call_players.remove(player)
                        print(f" call_players.remove = {player.name}")
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
                            print("\nПЕРЕХОДИМ КО ФЛОПУ: ")
                            for cpl in call_players:
                                print(f"count_players = {cpl.name}, position = {cpl.position}")
                            print(f"fold_count = {fold_count}")
                            print(f"call_count = {call_count}")
                            print(f"raise_count = {raise_count}")
                            return call_players, pot
                            # flag = False
                            # break
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
                    print(f"raise_count = {raise_count}\n")
                    if players_raise and fold_count + raise_count + call_count == count_players:
                        print("\nПЕРЕХОДИМ КО ФЛОПУ: ")
                        for cpl in call_players:
                            print(f"count_players = {cpl.name}, position = {cpl.position}\n")
                        return call_players, pot
                        # flag = False
                        # break
                    # print(f"next(iter(call_players) = {next(iter(call_players))}")
                    # if players_raise and next(iter(call_players)) == players_raise[0]:
                    #     print(f"next(iter(call_players) = {next(iter(call_players))}")
                    #     flag = False
                    # players_raise.clear()
                case 3:
                    # print(f"\npot = {pot} бб")
                    player.bet = float(input(f"Введите размер ставки от 2 до {player.stack} бб: "))
                    # dif = player.bet - player.share
                    last_bet = player.bet
                    pot += last_bet - player.share
                    player.share = player.bet

                    player.stack -= last_bet
                    print(f"\npot = {pot} бб")
                    print(f"Игрок {player.name} повышает ставку на {last_bet} бб\n")
                    raise_count = 1
                    call_count = 0
                    players_raise.append(player)
                    if players_raise:
                        call_players.clear()
                        # call_count = 0
                        players_raise.clear()
                    call_players.append(player)
                    players_raise.append(player)
                    for cpl in call_players:
                        print(f"call_players = {cpl}")
                    print(f"fold_count = {fold_count}")
                    print(f"call_count = {call_count}")
                    print(f"raise_count = {raise_count}\n")
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


# flop_players = preflop_action()[0]
# pot_flop = preflop_action()[1]

# print(f"Пот - {pot_flop}")
# for player in flop_players:
#     print(f"Игрок {player.name} на позиции {player.position} со стеком {player.stack}")
# print(type(preflop_action()))
flop_players, flop_pot = preflop_action()
print("\nФЛОП: ")
for plf in flop_players:
    print(f"Игрок {plf.name} на позиции {plf.position} со стеком {plf.stack}")
print(f"Пот на флопе - {flop_pot}")


# position

def board_action(flop_players_arg, pot_arg):
    flop_players_arg.sort(key=lambda p: BOARD_MAP[p.position])
    count_players = len(flop_players_arg)
    fold_count = 0
    call_count = 0
    raise_count = 0
    players_to_remove = []
    check_players = []
    call_players = []
    players_raise = []
    flag = True
    while flag:
        for player in flop_players_arg:
            player.share = 0
            print(f"Игрок {player.name} (позиция {player.position}) ходит со стеком {player.stack} бб")
            action = float(
                input(f"{player.name}, выберите действие (0 - fold, 1 - check, 2 - call, 3 - raise, 4 - all_in): "))
            match action:
                case 0:
                    fold_count += 1
                    print(f"Игрок {player.name} сбрасывает карты\n")
                    # players_to_remove.append(player)
                    if player in call_players:
                        call_players.remove(player)
                        print(f"call_players.remove = {player.name}")
                    for player_removed in players_to_remove:
                        print(f"player_removed = {player_removed.name}")
                        print(f"count_of_removed_players = {len(players_to_remove)}")
                        print(f"players_sort[0].name = {flop_players_arg[0].name}\n")
                        print()
                    if len(flop_players_arg) - len(players_to_remove) == 1 and raise_count == 0:
                        print(f"Игрок {flop_players_arg[-1].name} выиграл основной банк: {pot_arg} бб")
                        return pot_arg
                        # flag = False
                        # break
                    # elif len(players_sort) - fold_count == 1 and players_raise:
                    elif players_raise and fold_count + raise_count + call_count == count_players:
                        if fold_count == count_players - 1:
                            print(f"Игрок {players_raise[0].name} выиграл основной банк: {pot_arg} бб")
                            return pot_arg
                            # flag = False
                            # break
                        else:
                            # print("\nПЕРЕХОДИМ К ТЕРНУ: ")
                            for cpl in call_players:
                                print(f"count_players = {cpl.name}, position = {cpl.position}")
                            print(f"fold_count = {fold_count}")
                            print(f"call_count = {call_count}")
                            print(f"raise_count = {raise_count}\n")
                            return call_players, pot_arg
                            # flag = False
                            # break
                    elif players_raise and fold_count == count_players - 1:
                        print(f"Игрок {players_raise[0].name} выиграл основной банк: {pot_arg} бб")
                        return pot_arg
                        # flag = False
                        # break
                    print(f"fold_count = {fold_count}")
                    print(f"call_count = {call_count}")
                    print(f"raise_count = {raise_count}\n")
                    print(f"\npot = {pot_arg} бб")
                    if len(check_players) + fold_count == count_players:
                        return check_players, pot_arg
                case 1 if not players_raise:
                    print(f"Игрок {player.name} говорит чек и пропускает ход\n")
                    print(f"\npot = {pot_arg} бб")
                    check_players.append(player)
                    if len(check_players) == count_players or len(check_players) + fold_count == count_players:
                        # print("\nПЕРЕХОДИМ К ТЕРНУ: ")
                        for cpl in check_players:
                            print(f"count_players = {cpl.name}, position = {cpl.position}")
                        print(f"fold_count = {fold_count}")
                        print(f"check_players = {check_players}")
                        print(f"call_count = {call_count}")
                        print(f"raise_count = {raise_count}")
                        flop_players_arg.clear()
                        return check_players, pot_arg
                case 2:
                    print(f"Игрок {player.name} уравнивает ставку\n")
                    print(f"\npot = {pot_arg} бб")
                    call_count += 1
                    dif_to_call = last_bet - player.share
                    player.share = dif_to_call
                    pot_arg += dif_to_call
                    player.stack -= dif_to_call
                    print(f"player.stack = {player.stack}")
                    print(f"\n pot = {pot_arg} бб, {player.name} stack = {player.stack}")
                    call_players.append(player)
                    if call_players:
                        for cpl in call_players:
                            print(f"call_players = {cpl}")
                    print(f"fold_count = {fold_count}")
                    print(f"call_count = {call_count}")
                    print(f"raise_count = {raise_count}\n")
                    if players_raise and fold_count + raise_count + call_count == count_players:
                        # print("\nПЕРЕХОДИМ К ТЕРНУ: ")
                        for cpl in call_players:
                            print(f"count_players = {cpl.name}, position = {cpl.position}")
                        return call_players, pot_arg
                        # flag = False
                        # break
                    # print(f"next(iter(call_players) = {next(iter(call_players))}")
                    # if players_raise and next(iter(call_players)) == players_raise[0]:
                    #     print(f"next(iter(call_players) = {next(iter(call_players))}")
                    #     flag = False
                    # players_raise.clear()
                case 3:
                    # print(f"\npot = {pot} бб")
                    player.bet = float(input(f"Введите размер ставки от 2 до {player.stack} бб: "))
                    # dif = player.bet - player.share
                    last_bet = player.bet
                    pot_arg += last_bet - player.share
                    player.share = player.bet

                    player.stack -= last_bet
                    print(f"\npot = {pot_arg} бб")
                    print(f"Игрок {player.name} повышает ставку на {last_bet} бб\n")
                    raise_count = 1
                    call_count = 0
                    players_raise.append(player)
                    if players_raise:
                        call_players.clear()
                        check_players.clear()
                        # call_count = 0
                        players_raise.clear()
                    call_players.append(player)
                    players_raise.append(player)
                    for cpl in call_players:
                        print(f"call_players = {cpl}")
                    print(f"fold_count = {fold_count}")
                    print(f"call_count = {call_count}")
                    print(f"raise_count = {raise_count}\n")
                case 4:
                    # print(f"\n pot = {pot} бб")
                    print(f"Игрок {player.name} идет all-in\n")
    return flop_players_arg, pot_arg


flop_result = board_action(flop_players, flop_pot)

# Проверка типа результата
if isinstance(flop_result, tuple):
    turn_players, turn_pot = flop_result
    print("\nПЕРЕХОДИМ К ТЕРНУ: \n")
    turn_result = board_action(turn_players, turn_pot)
    if isinstance(turn_result, tuple):
        river_players, river_pot = turn_result
        print("\nПЕРЕХОДИМ К РИВЕРУ: \n")
        river_result = board_action(river_players, river_pot)
        if isinstance(river_result, tuple):
            river_players, river_pot = river_result
            print("\nОТКРЫВАЕМ КАРТЫ: \n")
#     if river_players:
#         print("\nВСКРЫВАЕМ КАРТЫ: \n")
#         # Вызываем действие для терна
#         board_action(river_players, river_pot)
#     else:
#         print("Все игроки сбросили карты, игра завершена.")
# else:
#     print("Игра завершена.")

# print(board_action(flop_players, flop_pot))
# if type(board_action(flop_players, flop_pot)) == tuple:
#     print("\nПЕРЕХОДИМ К ТЕРНУ: \n")


# turn_players, turn_pot = board_action(flop_players, flop_pot)

# board_action(turn_players, turn_pot)

# TODO условия хода на префлопе - у кого старше индекс позиции, тот ходит первым
# TODO условия хода после префлопа - первый ходит малый блайнд (SB), далее BB и остальные позиции в порядке
# TODO их индексов. КРОМЕ ХЕДЗ-АПА. Там первый ходит ББ!!!
# TODO создать словари для позиции ПРЕФЛОП и ПОСЛЕ ПРЕФЛОПА!!!
