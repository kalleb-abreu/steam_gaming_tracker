import requests


class APIClient:
    def __init__(self, api_key: str, api_endpoint: str, default_params: dict):
        """Initialize the API client.

        Parameters
        ----------
        api_key : str
            The Steam API key for authentication
        api_endpoint : str
            The base URL endpoint for the Steam API
        default_params : dict
            Default query parameters to include in requests

        Returns
        -------
        None
        """
        self.api_key = api_key
        self.api_endpoint = api_endpoint
        self.default_params = default_params

    def get_owned_games(self, steam_id: str) -> list[dict]:
        """Get list of games owned by Steam user.

        Parameters
        ----------
        steam_id : str
            The Steam ID of the user to get games for

        Returns
        -------
        list[dict]
            List of dictionaries containing game information
            Each dict has 'appid' and 'name' keys at minimum
        """
        params = self.default_params
        params["key"] = self.api_key
        params["steamid"] = steam_id
        response = requests.get(self.api_endpoint, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch games: {response.status_code} {response.text}")
        return response.json()
