# Standard library imports
import os

# Third-party imports
from dotenv import load_dotenv

# Local imports
import src.api_requests as api_requests
import src.utils as utils

# Load environment variables
load_dotenv("config/steam.env")

# Configure API settings
STEAM_API_KEY = os.getenv("STEAM_API_KEY")
STEAM_API_ENDPOINT = os.getenv("STEAM_API_ENDPOINT") 
STEAM_ID = os.getenv("STEAM_ID")
DEFAULT_PARAMS = dict(param.split('=')
                     for param in os.getenv("DEFAULT_PARAMS").split('&'))

# Initialize API client
api_client = api_requests.APIClient(
    STEAM_API_KEY, STEAM_API_ENDPOINT, DEFAULT_PARAMS)

# Fetch and process games data
games = api_client.get_owned_games(STEAM_ID)
exclude = utils.load_exclude("config/exclude.json")
df_games = utils.filter_games(games, exclude, ["appid", "name"])

# Save results
utils.save_csv(df_games.copy(), "out/games.csv")
