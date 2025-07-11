import socket
from cryptography.fernet import Fernet

# Use the same Fernet key as the server
FERNET_KEY = "sPRR3RJ6GqTQaAxhdo3AElG5V7-WvMGpdVR14ONcJ6I=".encode()
cipher = Fernet(FERNET_KEY)

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))
    print("Connected to the server! Type 'exit' to disconnect.")

    try:
        while True:
            message = input()
            if message.lower() == "exit":
                encrypted_message = cipher.encrypt(message.encode())
                client.send(encrypted_message)
                print("Logging out...")
                break

            encrypted_message = cipher.encrypt(message.encode())
            client.send(encrypted_message)

            encrypted_response = client.recv(1024)
            if not encrypted_response:
                break

            decrypted_response = cipher.decrypt(encrypted_response).decode()
            print(f"Server: {decrypted_response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print("Disconnected from the server.")

if __name__ == "__main__":
    start_client()
