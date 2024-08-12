from typing import List, Optional


class Player:
    def __init__(self, player_name: Optional[str], pocket_hand: List[str] = None):
        self.pocket_hand = pocket_hand
        self.player_name = player_name

    def __str__(self):
        return f"{self.player_name}: {', '.join(self.pocket_hand)}"

    # def seven_cards(self, pocket_hand_arg: List[str], river_arg: List[str]):
    #     hand_instance = [pocket_hand_arg.extend(river_arg)
    #     pass
    