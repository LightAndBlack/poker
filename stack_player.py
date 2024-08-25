from typing import Optional


class Player:
    def __init__(self, player_name: Optional[str], stack: float, position: Optional[str] = None, bet: Optional[float] = None, action: Optional[any] = None, share: Optional[float] = None, pocket_card: Optional[str] = None, final_combo: Optional[str] = None, showdown_status: Optional[bool] = True):
        self.name = player_name
        self.stack = stack
        self.position = position

    def __str__(self):
        return f"Стек игрока {self.name}: {self.stack} бб"

