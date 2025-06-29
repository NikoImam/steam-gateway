import time
import requests

from Models.SteamUser import SteamUser
import logging

logging.basicConfig(level=logging.ERROR)  # Или INFO, DEBUG, в зависимости от нужд
logger = logging.getLogger(__name__)

def get_steam_user_info(steam_id : int, api_key : str) -> SteamUser :
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    })

    user_url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={steam_id}"

    # Получаем информацию о играх пользователя
    games_url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={steam_id}"

    try:
        # Запрос информации о пользователе
        user_response = session.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        time.sleep(2)

        # Запрос информации о играх
        games_response = session.get(games_url)
        games_response.raise_for_status()
        games_data = games_response.json()

        # Извлекаем нужные данные
        player = user_data['response']['players'][0]
        game_count = games_data['response']['game_count'] if 'game_count' in games_data['response'] else 0

        games = []

        for game in games_data['response']['games']:
            games.append(game['appid'])

        return SteamUser (steam_id,
                          player.get('personaname', 'Unknown'),
                          player.get('avatarfull', ''),
                          player.get('profileurl', ''),
                          game_count)

    except Exception as e:
        logger.error(f"Ошибка при получении данных Steam для ID {steam_id}: {e}\n", exc_info=True)
        raise

def get_steam_user_owned_games(steam_id : int, api_key : str) -> list[int]:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    })
    # Получаем информацию о играх пользователя
    games_url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={steam_id}"

    try:
        # Запрос информации о играх
        games_response = session.get(games_url)
        games_response.raise_for_status()
        games_data = games_response.json()

        # Извлекаем нужные данные
        games = []

        for game in games_data['response']['games']:
            games.append(game['appid'])

        return games

    except Exception as e:
        logger.error(f"Ошибка при получении игр из Steam для ID {steam_id}: {e}\n", exc_info=True)
        raise

def get_steam_user_wishlist(steam_id : int, api_key : str) -> list[int]:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    })
    # Получаем информацию о играх пользователя
    wishlist_url = f"https://api.steampowered.com/IWishlistService/GetWishlist/v1/?key={api_key}&steamid={steam_id}"

    try:
        # Запрос информации о играх
        games_response = session.get(wishlist_url)
        games_response.raise_for_status()
        games_data = games_response.json()

        # Извлекаем нужные данные
        games = []

        for item in games_data['response']['items']:
            games.append(item['appid'])

        return games

    except Exception as e:
        logger.error(f"Ошибка при получении вишлиста из Steam для ID {steam_id}: {e}\n", exc_info=True)
        raise