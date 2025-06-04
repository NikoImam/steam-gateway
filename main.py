from steam import Steam
from decouple import config

KEY = config('STEAM_API_KEY')

steam = Steam(KEY)

user = steam.users.get_user_details('76561198949189790')
print(user)