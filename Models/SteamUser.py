from dataclasses import dataclass
from typing import Optional

@dataclass
class SteamUser:
    steam_id: str
    username: str
    avatar_url: str
    profile_url: str
    game_count: int
    status: str
    error: str

    def __init__(self,
                 steam_id : str,
                 username : str,
                 avatar_url : str,
                 profile_url : str,
                 game_count : int,
                 status : str):
        self.steam_id = steam_id
        self.username = username
        self.avatar_url = avatar_url
        self.profile_url = profile_url
        self.game_count = game_count
        self.status = status
