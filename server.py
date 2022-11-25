#소켓 프로그래밍에 필요한 api제공 모듈
import socket

ip = '192.168.0.216'
port = 50001

# 소켓 객체 생성
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 소켓 주소 정보 할당
server_socket.bind((ip,port))

# 연결 리스닝(동시접속)수 설정
server_socket.listen(10)

# 연결 수락 (클라리언트 정보(소캣,주소)반환)
client_socket,address = server_socket.accept()
print(abc)
