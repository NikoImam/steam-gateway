from dataclasses import dataclass
from typing import Optional

@dataclass
class SteamUser:
    steam_id: int
    username: str
    avatar_url: str
    profile_url: str
    game_count: int

    def __init__(self,
                 steam_id : int,
                 username : str,
                 avatar_url : str,
                 profile_url : str,
                 game_count: int):
        self.steam_id = steam_id
        self.username = username
        self.avatar_url = avatar_url
        self.profile_url = profile_url
        self.game_count = game_count

    def __str__(self):
        return f"{self.username} ({self.steam_id}) | {self.game_count} игр"
