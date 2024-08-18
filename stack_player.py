from typing import Optional


class Player:
    def __init__(self, player_name: str, stack: float, position: Optional[str] = None):
        self.name = player_name
        self.stack = stack
        self.position = position

    def __str__(self):
        return f"Стек игрока {self.name}: {self.stack} бб"

