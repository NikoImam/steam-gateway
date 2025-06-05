from dataclasses import dataclass
from typing import Optional

@dataclass
class SteamUser:
    steam_id: str
    username: str
    avatar_url: str
    profile_url: str
    games: list[int]

    def __init__(self,
                 steam_id : str,
                 username : str,
                 avatar_url : str,
                 profile_url : str,
                 games : list[int]):
        self.steam_id = steam_id
        self.username = username
        self.avatar_url = avatar_url
        self.profile_url = profile_url
        self.games = games

    def __str__(self):
        return f"{self.username} ({self.steam_id})"
