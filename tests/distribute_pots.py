from typing import Optional


class Player:
    def __init__(self, name: [str], position: [str], invested_chips: [float], power_combo: [float],
                 win_size_pot: Optional[float] = 0, stack_rest: Optional[float] = 0):
        self.name = name
        self.position = position
        self.stack_rest = stack_rest
        self.invested_chips = invested_chips
        self.power_combo = power_combo
        self.win_size_pot = win_size_pot

    def __str__(self):
        return f"Игрок {self.name} на позиции {self.position} поставил ALL_IN = {self.invested_chips} бб, " \
               f"сила комбинации = {self.power_combo}, размер выигрыша = {self.win_size_pot} бб"


# TODO РЕАЛИЗОВАТЬ ДОП ПРОВЕРКУ - СУММА ВСЕХ вложенных фишек д. б. равна сумме ВСЕХ ВЫИГРЫШЕЙ в конце раздачи!!!!
# TODO ТЕСТ - РАЗНЫЕ силы победителей

# 1
# TODO ВСЕГО 591                                    591 = 40 + 142 + 409

player1 = Player("Player1", "BB", 175, 326)  # TODO 40, player.stack_rest = 40
player2 = Player("Player2", "SB", 135, 424)  # TODO 142, player.stack_rest = 59
player3 = Player("Player3", "BTN", 100, 113)
player4 = Player("Player4", "CO", 76, 521)   # TODO 409
player5 = Player("Player5", "HJ", 65, 231)
player6 = Player("Player6", "UTG", 40, 224)

# TODO ВСЕГО 831                                       831
# player1 = Player("Player1", "BB", 175, 326)   # TODO 80, player.stack_rest = 40
# player2 = Player("Player2", "SB", 135, 424)   # TODO 177, player.stack_rest = 59
# player3 = Player("Player3", "BTN", 340, 113)  # TODO 165,
# player4 = Player("Player4", "CO", 76, 521)    # TODO 409
# player5 = Player("Player5", "HJ", 65, 231)
# player6 = Player("Player6", "UTG", 40, 224)


# TODO ТЕСТ - ОДИНАКОВЫЕ СИЛЫ победителей, РАЗНЫЕ стеки!

# TODO ВСЕГО 591                                       591 = 40 + 346,5 + 204,5
# player1 = Player("Player1", "BB", 175, 326) # TODO = 40
# player2 = Player("Player2", "SB", 135, 521) #  = 204,5 + 24 (player3.rest_stack) + (135 - 76 = 59) * 2 (2, 1) =
#                                               TODO = 346,5
# player3 = Player("Player3", "BTN", 100, 113) # TODO player stack.rest = 24 уйдет игроку 2
# player4 = Player("Player4", "CO", 76, 521) #  = (76 * 4 (4,3,2,1) + 65 + 40) /
#                                               len(list[76, 76(от 135) упорядочить по возрастанию нужно функцией] =
#                                       TODO 333 / 2 = 204,5

# player5 = Player("Player5", "HJ", 65, 231)
# player6 = Player("Player6", "UTG", 40, 224)


# player1 = Player("Player1", "BB", 175, 326)
# player2 = Player("Player2", "SB", 135, 521)
# player3 = Player("Player3", "BTN", 100, 113)
# player4 = Player("Player4", "CO", 76, 521)
# player5 = Player("Player5", "HJ", 65, 231)
# player6 = Player("Player6", "UTG", 40, 224)


# TODO ТЕСТ - ОДИНАКОВЫЕ СИЛЫ победителей, РАЗНЫЕ стеки 3 победителя, 3 на 2 победителя, 1 проигравший!


# TODO ТЕСТ - ОДИНАКОВЫЕ СИЛЫ победителей, ОДИНАКОВЫЕ стеки!

# TODO а если одинаковые значения? В том числе ВСЕ???? Написать автотесты! И сверять с точными ответами!
# TODO - V использовал РЕКУРСИЮ, так как не знал наверняка, сколько побочных банков нужно будет создать!
# TODO тест варианта, когда у нескольких одинаковая сила руки, а у других слабее и разные стеки!!!!!!!!!!!!!!!!
# TODO нужно создавать отдельные списки победителей, смотри еще на РАЗЛИЧИЯ СТЕКОВ ПОБЕДИТЕЛЕЙ!!!!!!!!!!!!!!!!


all_in_list = [player6, player5, player4, player3, player2, player1]


class Pot:

    @staticmethod
    def get_main_winner(self):
        players_by_power = sorted(all_in_list, key=lambda player: player.power_combo, reverse=True)
        return players_by_power[0]

    @staticmethod
    def distribute_pots(all_in_list_arg):
        players_by_power = sorted(all_in_list_arg, key=lambda player: player.power_combo, reverse=True)
        if players_by_power[0] == Pot.get_main_winner(all_in_list_arg):
            main_pot = players_by_power[0].invested_chips
            print(
                f"players_by_power[0] == Pot.get_main_winner(all_in_list_arg) = {Pot.get_main_winner(all_in_list_arg)}, ПОЭТОМУ main_pot = {main_pot}")
            print(f"players_by_power_arg[0] = {players_by_power[0]}")
        else:
            main_pot = players_by_power[0].stack_rest
            print(f"players_by_power[0].stack_rest = {players_by_power[0].stack_rest}")
            print(f"main_pot = {main_pot}")
        rest_stacks_lists = []

        print("\nНАЧАЛО ЦИКЛА: \n")
        for i, player_main in enumerate(players_by_power[1:], start=1):
            if players_by_power[0].power_combo == players_by_power[i].power_combo:
                players_by_power[0].stack_rest = players_by_power[0].invested_chips
                players_by_power[i].stack_rest = players_by_power[i].invested_chips
                print(f"Прохожу ПЕРВЫЙ if, i = {i}")
            elif players_by_power[0].power_combo > players_by_power[i].power_combo:
                if players_by_power[0].invested_chips >= players_by_power[i].invested_chips:
                    if players_by_power[0] == Pot.get_main_winner(all_in_list_arg):
                        main_pot += players_by_power[i].invested_chips
                        print(f"players_by_power_arg[{i}].invested_chips = {players_by_power[i].invested_chips}")
                        print(f"main_pot = {main_pot}")
                    else:
                        main_pot += players_by_power[i].stack_rest
                        print(f"players_by_power_arg[{i}].stack_rest = {players_by_power[i].stack_rest}")
                        print(f"main_pot = {main_pot}")
                elif players_by_power[0].invested_chips < players_by_power[i].invested_chips:
                    if players_by_power[0] == Pot.get_main_winner(all_in_list_arg):
                        main_pot += players_by_power[0].invested_chips
                        players_by_power[i].stack_rest = players_by_power[i].invested_chips - players_by_power[
                            0].invested_chips
                        rest_stacks_lists.append(players_by_power[i])
                        print(f"players_by_power[{i}].stack_rest = {players_by_power[i].stack_rest}")
                        print(f"main_pot = {main_pot}")
                    else:
                        main_pot += players_by_power[0].stack_rest
                        players_by_power[i].stack_rest = players_by_power[i].stack_rest - players_by_power[
                            0].stack_rest
                        rest_stacks_lists.append(players_by_power[i])
                        print(f"players_by_power[{i}].stack_rest = {players_by_power[i].stack_rest}")
                        print(f"main_pot = {main_pot}")
        players_by_power[0].stack_rest += main_pot
        if rest_stacks_lists:
            print("\nСписок игроков, участвующих в розыгрыше ПОБОЧНЫХ банков: \n")
            for i, player in enumerate(rest_stacks_lists):
                print(f"player.name = {player.name}, player.position = {player.position}, "
                      f"player.power_combo = {player.power_combo}, player.invested_chips = {player.invested_chips}, "
                      f"player.stack_rest = {player.stack_rest}")
            print("\n\n")

        # Рекурсивно обрабатываем игроков с остатками стеков
        if rest_stacks_lists:
            Pot.distribute_pots(rest_stacks_lists)


Pot.distribute_pots(all_in_list)
