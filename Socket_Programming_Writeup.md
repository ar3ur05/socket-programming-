# 🔌 Socket Programming Writeup

## Overview

The goal of this task was to create a simple **TCP chat application** with **symmetric encryption** using **Python**.  
Encryption is implemented using **Fernet** from the `cryptography` library.

A **socket** acts as an endpoint that facilitates communication over a network. In this project, we were required to provide symmetric encryption, meaning the same key is used for both **encryption** and **decryption**.

> 📝 Both `server.py` and `client.py` scripts are included, along with screenshots of the working application.

To run the application:

1. Start the server using `server.py`.
2. Run the client using `client.py`.

---

## 🖥 Server Logic

### 1. Fernet Key Setup

A **predefined Fernet key** is shared between the client and server.  
This key is used to initialize the Fernet cipher:
```python
cipher = Fernet(fernet_key)
```

---

### 2. Functions Used

#### `handle_client(conn, addr)`

- **`conn`**: socket object of the connected client  
- **`addr`**: IP address and port of the client

**Functionality:**

- When a client connects, it prints the client IP and port.
- Waits for incoming encrypted messages.
- Decrypts received messages using the shared key.
- Displays the original (decrypted) message.
- If the client sends `"exit"`, the loop breaks and connection is closed.
- Errors like disconnection are handled gracefully.
- Ensures that the socket is properly closed using a `finally` block.

#### `start_server()`

- Uses `AF_INET` (IPv4) and `SOCK_STREAM` (TCP).
- Binds to `localhost:12345` using:
  ```python
  server.bind(('localhost', 12345))
  ```
- Listens for incoming connections.
- For each client, creates a new thread via `threading.Thread()` to allow concurrent connections.

```python
if __name__ == "__main__":
    start_server()
```
This ensures the server starts only when the script is executed directly.

---

## 💻 Client Logic

- Uses the **same Fernet key** as the server.
- Imports `socket` and `Fernet`.

### Function: `start_client()`

**Functionality:**

- Connects to the server using `connect()`.
- Prompts the user to input messages.
- If user types `"exit"`, logs out and closes connection.
- Otherwise:
  - Encrypts the message using Fernet.
  - Sends it to the server.
  - Waits for the server's response.
  - Decrypts and displays the server’s message.
- Handles errors like lost connections.
- Ensures the connection is closed properly in a `finally` block.

---

## ✅ Summary

- A **multi-threaded, encrypted TCP chat application** was built using Python sockets and Fernet encryption.
- Secure communication is established using a **shared symmetric key**.
- Proper **error handling**, **clean shutdown**, and **client-server threading** are implemented.
