# Websocket Server

Websockets are used to communicate efficiently through the web. Websockets can be used for communication within two systems of the same computer, with different computers in the same network, or even to communicate across networks. This code offers server capabilities for a computer to manage websocket connection.

## First Installation (Linux)
1. Create a virtual environment with `python -m venv .venv`
2. Activate the virtual environment with `source .venv/bin/activate`
3. Install packages from `pyproject.toml` with `pip install -e .`
4. Run `python ./src/CTR_websockets/serve.py` to start the websocket server

## Subsequent Runs
1. Activate the virtual environment with `source .venv/bin/activate`
2. Run `python ./src/CTR_websockets/serve.py` to start the websocket server

## Installing Further Packages

If you wish to install more packages, make sure to add them to `pyproject.toml` in the `dependencies` section.
