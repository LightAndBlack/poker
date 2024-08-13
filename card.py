class Card:
    RANK_MAP = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
        }

    SUIT_MAP = {
        2: 'c',
        4: 'd',
        8: 'h',
        16: 's'
    }

    def __init__(self, rank, suit):
        self.rank = 14 if rank == 1 else rank
        self.suit = suit

    def __str__(self):
        rank = self.RANK_MAP[self.rank]
        suit = self.SUIT_MAP[self.suit]
        return "{0}{1}".format(rank, suit)

    @staticmethod
    def get_card_value(card):
        return Card.RANK_MAP[card[:-1]]

    @staticmethod
    def get_rank_value(rank):
        return Card.RANK_MAP[rank]


# примеры создания карт
# card = Card(11, 2)
# print(card.rank, card.suit)
# print(str(card))

x = 'A'
print(Card.get_rank_value(x))
