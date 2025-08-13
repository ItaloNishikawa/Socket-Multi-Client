import socket;
import time;

HOST = "127.0.0.2";
PORT = 5556;

server_HOST = "127.0.0.1";
server_PORT = 5555;

def start_client():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((server_HOST, server_PORT)); 
                username= input("Digite seu nome de usuário: ");
                client_socket.sendall(username.encode());

                while True:
                    message = input("Digite aqui...")
                            
                    if message.lower() == 'sair':
                        print("Encerrado a conexão...")
                        break
                    client_socket.sendall(message.encode());

        except ConnectionRefusedError:
            print("Não foi possível conectar ao servidor. Tentando novamente em 5 segundos...");
            time.sleep(5);
        except Exception as e:
            print(f"Ocorreu um erro: {e}");


if __name__ == "__main__":
    start_client();    