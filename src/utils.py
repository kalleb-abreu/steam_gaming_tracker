import pandas as pd
import json


def filter_games(games: dict, exclude: dict, columns: list[str]) -> pd.DataFrame:
    """Filter games based on exclusion criteria and return selected columns.

    Parameters
    ----------
    games : dict
        Dictionary containing Steam API response with games data
    exclude : dict
        Dictionary with appids and names to exclude
    columns : list[str]
        List of column names to include in output DataFrame

    Returns
    -------
    pd.DataFrame
        DataFrame with filtered games and selected columns, sorted by name
    """
    df = pd.DataFrame(games["response"]["games"])
    df = df[~df["appid"].isin(exclude["exclude"]["appids"])]
    df = df[columns]

    return df.sort_values(by="name", ascending=True)


def save_csv(df: pd.DataFrame, path: str) -> None:
    """Save DataFrame to CSV file, merging with existing data if present.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing game data to save
    path : str
        File path where CSV should be saved

    Returns
    -------
    None
    """
    df.columns = ["App ID", "Name"]
    try:
        existing_df = pd.read_csv(path)
        existing_cols = existing_df.columns.tolist()

        for col in existing_cols:
            if col not in df.columns:
                df.loc[:, col] = None

        df = pd.concat([existing_df, df]).drop_duplicates(
            subset=["App ID"], keep="first")
        df = df.sort_values(by="Name", ascending=True)
    except FileNotFoundError:
        import os
        os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def load_exclude(path: str) -> dict:
    """Load game exclusion configuration from JSON file.

    Parameters
    ----------
    path : str
        Path to JSON configuration file

    Returns
    -------
    dict
        Dictionary containing game exclusion configuration
    """
    with open(path, "r") as f:
        return json.load(f)
