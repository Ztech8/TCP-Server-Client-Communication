# TCP Server-Client Communication

## Overview

This repository contains a basic implementation of a TCP server and client in Python. The server listens for incoming connections, and the client connects to the server. The server can continuously send messages to the client until the user types 'exit' to close the connection.

## Prerequisites

- Python 3.x

## Usage

### Server

1. Open a terminal.
2. Navigate to the directory containing the `server.py` file.
3. Run the server script:

    ```bash
    python server.py
    ```

4. The server will start listening for incoming connections.

### Client

1. Open another terminal.
2. Navigate to the directory containing the `client.py` file.
3. Run the client script:

    ```bash
    python client.py
    ```

4. The client will connect to the server, and you can start exchanging messages.

## Communication

- The server can send messages to the client by typing messages in the server terminal.
- To close the connection, type 'exit' in the server terminal.

## Notes

- This is a basic example and does not handle exceptions or errors for robustness.
- Ensure that your firewall settings allow communication on the specified port.

## License

This project is licensed under the [MIT License](LICENSE).

---
