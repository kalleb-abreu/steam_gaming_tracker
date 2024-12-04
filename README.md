# Steam Gaming Tracker

A Python application that fetches and tracks your Steam game library, allowing you to filter out specific games and export the results to CSV.

## Description

Steam Gaming Tracker is a tool that connects to the Steam Web API to retrieve your owned games list. It provides functionality to:
- Fetch all games owned by a specified Steam user;
- Filter out unwanted games using a configuration file;
- Export the filtered game list to CSV format.

## Prerequisites

- Python 3.8 or higher;
- A Steam Web API key;
- Your Steam ID (64-bit format);
- Required Python packages (see requirements.txt).

## Features

- Retrieves complete game library from Steam API;
- Configurable game exclusion via JSON file;
- Sorts games alphabetically by name;
- CSV export.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kalleb-abreu/steam-gaming-tracker.git
   cd steam-gaming-tracker
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your Steam credentials:
   - Copy `config/steam.env.example` to `config/steam.env`;
   - Add your Steam API key and Steam ID to the file.

4. Configure game exclusions (optional):
   - Edit `config/exclude.json` to add game IDs or names you want to exclude.

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Check the output:
   - Generated CSV file will be in the `out` directory;
   - Games are sorted alphabetically.

## Configuration Files

### steam.env
Contains Steam API credentials and configuration:
- `STEAM_API_KEY`: Your Steam Web API key;
- `STEAM_ID`: Your Steam 64-bit ID;
- API endpoints and parameters.

### `exclude.json`
JSON file for configuring games to exclude:
- `appids`: List of Steam game IDs to exclude;
- `names`: List of game names to exclude.

## Output Format

The generated CSV file contains:
- `App ID`: Steam application ID;
- `Name`: Game name.

## Contributing

Feel free to submit issues, fork the repository and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.