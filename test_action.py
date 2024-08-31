from stack_player import Player
from test_game import start_hand, get_river, deck
from test_combo import all_hands, evaluate_combo, sort_cards

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
        player.showdown_status = True
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
final_hands = all_hands.values()
print(f"final_hands = {final_hands}")
for idx, player in enumerate(players):
    player.pocket_cards = list(all_hands.values())[idx][0:2]
    player.final_combo = list(all_hands.values())[idx]
    # print(player.name, player.position, player.stack, evaluate_combo(sort_cards(player.final_combo)))
    # print(f"final_hands = {final_hands}")
    # player.pocket_cards = final_hand[0:2]

river_cards = get_river()[0:5]
turn_cards = river_cards[0:4]
flop_cards = get_river()[0:3]
print(f"all_hands = {all_hands}")

# print(f"all_start_hands = {all_start_hands}")
# print(f"deck = {deck}")
print(flop_cards)
print(turn_cards)
print(river_cards)


def preflop_action():
    players_sort = sorted(players, key=lambda player_arg: players.index(player_arg), reverse=True)
    count_players = len(players_sort)
    raise_count = 0
    call_count = 0
    fold_count = 0
    all_in_count = 0
    pot = 1.5
    last_bet = 1
    players_raise = []
    call_players = []
    all_in_players = []
    flag = True
    while flag:
        for player in players_sort:
            print("Ваша рука - ", *player.pocket_cards)
            print(
                f"player_position для игрока {player.name} = {player.position}, player.share = {player.share}, player_stack = {player.stack}")
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
            elif player in players_to_remove:
                continue
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
                    player.showdown_status = False
                    print(f"Игрок {player.name} сбрасывает карты\n")
                    players_to_remove.append(player)
                    # if player in call_players:
                    #     call_players.remove(player)
                    #     print(f" call_players.remove = {player.name}")
                    # for player_removed in players_to_remove:
                    #     print(f"player_removed = {player_removed.name}")
                    #     print(f"count_of_removed_players = {len(players_to_remove)}")
                    #     print(f"players_sort[0].name = {players_sort[0].name}")
                    #     print()
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
                    if all_in_players and player.stack <= call_all_in:
                        all_in_players.append(player)
                        dif_to_call = player.stack
                        all_in_count += 1
                        player.stack = 0
                        pot += dif_to_call
                        if all_in_count + fold_count == count_players:
                            print(
                                f"Игрок {player.name} на позиции {player.position} идет all-in, стек игрока = {player.stack}, пот = {pot} ")
                            print("\nПЕРЕХОДИМ КО ФЛОПУ: ")
                            for cpl in all_in_players:
                                print(
                                    f"all_in_players = {cpl.name}, position = {cpl.position}, карты = {cpl.pocket_cards}\n")
                            return all_in_players, pot
                        print(
                            f"Игрок {player.name} на позиции {player.position} идет all-in, стек игрока = {player.stack}, пот = {pot} ")
                        continue
                    elif all_in_players and player.stack > call_all_in:
                        dif_to_call = call_all_in
                        player.stack -= call_all_in
                    else:
                        dif_to_call = last_bet - player.share
                    if player.position == 'BB' or player.position == 'SB' and player.share <= 1:
                        player.stack -= last_bet
                    else:
                        player.stack -= dif_to_call
                    player.share += dif_to_call
                    print(f"dif_to_call = {dif_to_call}")
                    pot += dif_to_call
                    # player.stack -= dif_to_call
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
                    if player.bet == player.stack:
                        all_in_players.append(player)
                        all_in_count += 1
                        player.stack = 0
                        pot += player.bet
                        call_all_in = player.bet
                        print(
                            f"Игрок {player.name} ставит {player.bet} бб и идет all-in остаток игрока = {player.stack}, ПОТ = {pot}")
                        continue
                    dif = player.bet - player.share
                    # player.share += dif
                    last_bet = player.bet
                    # pot += last_bet - player.share
                    if player.position == 'SB' and player.share <= 1:
                        player.stack -= player.bet
                        pot += last_bet - player.share
                        print(f"pot = {pot}")
                    elif player.position == 'SB' and player.share > 1:
                        player.stack -= dif
                        pot += last_bet - player.share
                        print(f"pot = {pot}")
                    elif player.position == 'SB' and player.bet == player.stack:
                        player.stack -= player.bet
                        pot += last_bet
                    elif player.position == 'BB' and player.share == 1:
                        player.stack -= player.bet
                        pot += last_bet - player.share
                    elif player.position == 'BB' and player.share > 1:
                        player.stack -= player.bet - player.share
                        pot += last_bet - player.share
                    # elif player.position == 'BB' and player.position == 'SB':
                    #     player.stack -= player.bet + player.share
                    #     pot += last_bet - player.share
                    #     print(f"pot = {pot}")
                    else:
                        pot += last_bet - player.share
                        player.stack -= dif
                    player.share = player.bet

                    print(f"\npot = {pot} бб")
                    print(f"Игрок {player.name} ставит {last_bet} бб, текущий стек = {player.stack} \n")
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
                    if player.stack == 0:
                        print(
                            f"Игрок {player.name} на позиции {player.position} идет all-in, стек игрока = {player.stack}, текущий банк = {pot}\n")
                        all_in_players.append(player)
                        call_all_in = player.bet
                case 4:
                    # print(f"\n pot = {pot} бб")
                    print(
                        f"Игрок {player.name} на позиции {player.position}идет all-in, стек игрока = {player.stack}, текущий банк = {pot}\n")

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
# flop_players, flop_pot = preflop_action()
# print("\nФЛОП: ")
# for plf in flop_players:
#     print(f"Игрок {plf.name} на позиции {plf.position} со стеком {plf.stack}")
# print(f"Пот на флопе - {flop_pot}")


# position

def board_action(board_players_arg, pot_arg):
    board_players_arg.sort(key=lambda p: BOARD_MAP[p.position])
    count_players = len(board_players_arg)
    fold_count = 0
    call_count = 0
    raise_count = 0
    players_to_remove = []
    check_players = []
    call_players = []
    players_raise = []
    all_in_players = []
    action = 1
    flag = True
    for player in board_players_arg:
        player.share = 0
    while flag:
        for player in board_players_arg:
            print(f"1-ая строка после префлопа - player.share = {player.share}")
            if len(all_in_players) == len(board_players_arg):
                return all_in_players, pot_arg
            if player.stack == 0:
                all_in_players.append(player)
                continue
            # if not raise_count:
            #     player.share = 0
            print("Ваша рука - ", *player.pocket_cards)
            print(f"Игрок {player.name} (позиция {player.position}) ходит со стеком {player.stack} бб")
            if player in players_to_remove:
                continue
            elif player not in all_in_players:
                action = float(
                    input(f"{player.name}, выберите действие (0 - fold, 1 - check, 2 - call, 3 - raise, 4 - all_in): "))
            match action:
                case 0:
                    fold_count += 1
                    player.showdown_status = False
                    print(f"Игрок {player.name} сбрасывает карты\n")
                    players_to_remove.append(player)
                    # if player in call_players:
                    #     call_players.remove(player)
                    #     print(f"call_players.remove = {player.name}")
                    # for player_removed in players_to_remove:
                    #     print(f"player_removed = {player_removed.name}")
                    #     print(f"count_of_removed_players = {len(players_to_remove)}")
                    #     print(f"players_sort[0].name = {flop_players_arg[0].name}\n")
                    #     print()
                    if len(board_players_arg) - len(players_to_remove) == 1 and raise_count == 0:
                        print(f"Игрок {board_players_arg[-1].name} выиграл основной банк: {pot_arg} бб")
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
                        board_players_arg.clear()
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
                    print(f"а сейчас player.share до ставки = {player.share}")
                    # dif = player.bet - player.share
                    last_bet = player.bet
                    pot_arg += last_bet - player.share
                    print(f"pot_arg = {pot_arg}")
                    if player.share == 0:
                        player.stack -= last_bet
                    else:
                        player.stack -= last_bet - player.share
                    print(f"player_stack = {player.stack}")
                    player.share = player.bet
                    print(f"а сейчас player.share после ставки = {player.share}")

                    print(f"\npot = {pot_arg} бб")
                    print(f"Игрок {player.name} ставит {last_bet} бб\n")
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
    return board_players_arg, pot_arg


preflop_result = preflop_action()

# Проверка типа результата
if isinstance(preflop_result, tuple):
    flop_players, flop_pot = preflop_result
    print("\nПЕРЕХОДИМ К ФЛОПУ: \n")
    print("ФЛОП: ", *flop_cards)
    flop_result = board_action(flop_players, flop_pot)
    # Проверка типа результата
    if isinstance(flop_result, tuple):
        turn_players, turn_pot = flop_result
        print("\nПЕРЕХОДИМ К ТЕРНУ: \n")
        print("ТЕРН: ", *turn_cards)
        turn_result = board_action(turn_players, turn_pot)
        if isinstance(turn_result, tuple):
            river_players, river_pot = turn_result
            print("\nПЕРЕХОДИМ К РИВЕРУ: \n")
            print("РИВЕР: ", *river_cards)
            river_result = board_action(river_players, river_pot)
            if isinstance(river_result, tuple):
                river_players, river_pot = river_result
                print("\nОТКРЫВАЕМ КАРТЫ: \n")
                win_power = 0
                win_players = []
                win_combo = []
                name_win_combo = ''
                for player in river_players:
                    if player.showdown_status:
                        combo_power = evaluate_combo(sort_cards(player.final_combo))
                        print(f"combo_power = {combo_power}")
                        combo = combo_power[0]
                        power = int(combo_power[1][1])
                        if power > win_power:
                            win_power = power
                            win_players.clear()
                            win_combo.clear()
                            win_players.append(player)
                            win_combo.extend(combo_power[1][0])
                            name_win_combo = combo
                        elif win_power == power:
                            win_players.append(player)
                        print(f"Игрок {player.name} на позиции {player.position} с оставшимся стеком {player.stack} бб собрал комбинацию {combo} - {combo_power[1][0]}")
                        # print(player.name, player.position, player.stack, evaluate_combo(sort_cards(player.final_combo)))
                print()
                print()
                if len(win_players) == 1:
                    win_players[0].stack += river_pot
                    print(f"Игрок {win_players[0].name} на позиции {win_players[0].position} ВЫИГРАЛ основной банк {river_pot} бб c комбинацией {name_win_combo} - {win_combo}")
                    print(f"Стек игрока {win_players[0].name} составляет {win_players[0].stack} бб")
                else:
                    print("Игроки ПОДЕЛИЛИ основной банк:")
                    for player in win_players:
                        player.stack += round(river_pot/len(win_players), 2)
                        print(f"Игрок {player.name} на позиции {player.position} ВЫИГРАЛ основной банк {player.stack} бб c комбинацией {name_win_combo} - {win_combo}")
                        print(f"Стек игрока {player.name} составляет {player.stack} бб")


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

# TODO - ВРОДЕ ПОФИКСИЛ Тестировать стеки блайндов на колах (B&B), исправлять ошибки - см. отчет по тестам
# TODO - ВРОДЕ КАК СДЕЛАЛ Определение победителя или ничьей, вывод и банк
# TODO Побочные банки, победитель внес больше, меньше. Определение побочных победителей
# TODO хэдз-ап
# TODO рефакторинг кода
# TODO оптимизация - битовые маски и сдвиги
