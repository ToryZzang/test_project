#소켓 프로그래밍에 필요한 api제공 모듈
import socket

ip = '192.168.0.10'
port = 50001

# 소켓 객체 생성
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 서버 연결
client_socket.connect((ip, port))
print("클라이언트 IP주소:".address[0])
