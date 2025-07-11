import socket
import threading
from cryptography.fernet import Fernet

# Use a pre-generated Fernet key
FERNET_KEY = "sPRR3RJ6GqTQaAxhdo3AElG5V7-WvMGpdVR14ONcJ6I=".encode()
cipher = Fernet(FERNET_KEY)

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    try:
        while True:
            encrypted_message = conn.recv(1024)
            if not encrypted_message:
                break

            decrypted_message = cipher.decrypt(encrypted_message).decode()
            if decrypted_message.lower() == "exit":
                print(f"Client {addr} has disconnected.")
                break

            print(f"Client: {decrypted_message}")

            # Get a response from the server user
            response = input("You: ")
            encrypted_response = cipher.encrypt(response.encode())
            conn.send(encrypted_response)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        print(f"Connection closed: {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 12345))
    server.listen(5)
    print("Server listening on 127.0.0.1:12345...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
