import socket;
import threading;

HOST = "127.0.0.1";
PORT = 5555;

def handle_client(conn, addr):
    print(f"Conectado por {addr}");
    with conn:
        try:
            username = conn.recv(1024).decode();
            print(f"{username} entrou no chat.");
            while True:
                data = conn.recv(1024);
                if not data:
                    break
                print(f"{username}: {data.decode()}");
        except ConnectionResetError:
            print(f"Conexão com {username} ({addr}) foi encerrada.");


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT));
        server_socket.listen();
        print(f"Server escutando no {HOST}:{PORT}...")

        while True:
            conn, addr = server_socket.accept();
            client_thread = threading.Thread(target=handle_client, args=(conn, addr));
            client_thread.start();
            print(f"Thread iniciada para {addr}");



if __name__ == "__main__":
    start_server();