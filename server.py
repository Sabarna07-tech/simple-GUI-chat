import socket
import threading
HOST = '192.168.29.213'
PORT = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
clients = []
nicknames = []

#broadcast
def broadcast(message):
    for client in clients:
        client.send(message)
def handel(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]}")
            broadcast(message)
        except:
            index =clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

#receive
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)
        clients.append(client)
        print (f"Nickname of the client is{nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("connected to the server".encode('utf-8'))
        thread = threading.Thread(target=handel, args=(client,))
        thread.start()
print("server running.....")
receive()




