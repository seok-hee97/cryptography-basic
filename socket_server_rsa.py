import socket

#접속 정보 설정
IP = "127.0.0.1"
PORT = 8080
SIZE =1024


#서버 소켓 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.connect((IP, PORT)) #서버에 접속
    server_socket.listen()

    #무한 루프 진입
    while True:
        client_socket, client_addr = server_socket.accept() #수신대기, 접속한 클라이언트 정보
        msg = client_socket.recv(SIZE)

        print("[{}] message : {}".format(client_addr,msg))

        client_socket.sendall("Welcome!".encode())


        client_socket.close()





    