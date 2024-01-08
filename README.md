# Kraken API Python Script README

## Description

This Python script allows you to interact with the Kraken API to retrieve your trade history. It uses the Kraken API's authentication method to access your account's trade information.

## Requirements

To run this script, you need:

- Python 3.x installed on your system.
- Kraken API Key and Secret obtained from your Kraken account.

## Installation

1. Clone or download this repository to your local machine.
2. Add the API key and secret key to the keys.py file.


## Configuration

1. Open the `keys.py` file and replace `api_key` and `api_sec` with your Kraken API Key and Secret.

```python
api_key = "your_api_key"
api_sec = "your_api_secret"
```

## Usage
Run the Python script in your terminal or preferred Python environment.
```
python kraken_bot.py
```

The script will access your Kraken account's trade history using the API.

## Implementation
The script uses the requests library to make API requests to Kraken.
It generates a signature for authentication based on your API Key and Secret.
It retrieves and prints your trade history from Kraken.


