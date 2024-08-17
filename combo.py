from test_game import players, river


class Combo:
    # print(type(river))
    # print(players)

    # print(start_hand.pocket_hand, type(start_hand.pocket_hand))
    # print(river, type)

    @staticmethod
    def get_combined_hands(players_dict, river_cards):
        """
        Создает объединенный список из стартовой руки каждого игрока и карт на ривере.

        :param players_dict: Словарь игроков, где ключ — имя игрока, значение — объект Player.
        :param river_cards: Список карт на ривере.
        :return: Словарь, где ключ — имя игрока, значение — объединенный список его карт и ривера.
        """
        combined_hands = {}
        for player_name, player in players_dict.items():
            # Объединяем стартовую руку игрока с ривером
            combined_hand = player.pocket_hand + river_cards
            combined_hands[player_name] = combined_hand
        return combined_hands

    # for start_hand in players.values():
    # print(get_combined_hands(players, river))
    # print(get_combined_hands(players, river)['Player 1'])

    # ниже пойдет логика сортировки рангов и мастей по убыванию, определение лучшей комбинации 5 карт из 7,
    # учитываю проверку: входят ли карманные руки в отсортированные по убыванию элементы списка, чтобы исключить
    # не оправданный дележ банка, если у каких-то игроков карманные руки будут усиливать готовые комбо из
    # 5 карт на столе - смотри user_story.txt (может точнее use_case?)
    # Если никто не усилися, то ничья иначе смотрим у кого лучшее усиление и определяем победителей
    # главного банка и побочных (если есть)

    # def seven_cards(self, river_arg, ):
    #     pass

    @classmethod
    def royal_flush(cls):
        # if Card.card.rank == 60:
        return 10

    @classmethod
    def straight_flush(cls):
        pass

    @classmethod
    def four_of_a_kind(cls):
        pass

    @classmethod
    def full_house(cls):
        pass

    @classmethod
    def flush(cls):
        pass

    @classmethod
    def straight(cls):
        pass

    @classmethod
    def three_of_a_kind(cls):
        pass

    @classmethod
    def two_pairs(cls):
        pass

    @classmethod
    def pair(cls):
        pass

    @classmethod
    def high_card(cls):
        pass

    pass
