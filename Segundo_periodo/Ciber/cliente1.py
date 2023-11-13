import socket
import threading
#função de recebimento de dados do cliente
def recebeDados(conn):
    try:
        while True:
        mensagem = conn.recv(1024).decode()
        print(mensagem)
    except:
        print("Erro no recebimento de mensagens do servidor...")
    return
#INFORMAÇÕES DO SERVIDOR
HOST = "127.0.0.1"
PORT = 9999
#QUERO ME CONECTAR EM 127.0.0.1:9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#COMO A CONEXÃO É TCP PRECISAMOS DE UM CONNECT
sock.connect((HOST, PORT)) #CONNECT ACENDE O ACCEPT DO SERVIDOR
#AGORA O CLIENTE ENVIA DADOS
nome = input("Informe o seu nome: ")
print("----- CHAT INICIADO -----")
#enviando nome para o servidor
sock.sendall(str.encode(nome))
#vamos inicializar a thread para o cliente ficar recebendo dados
threadRecebeDados = threading.Thread(target=recebeDados, args=[sock])
threadRecebeDados.start()
#vamos abrir um loop para o cliente ficar enviando dados para o Servidor
try:
    while True:
    mensagem = input('')
    print(f"{nome} >> {mensagem}")
    sock.sendall(str.encode(mensagem))
finally:
    sock.close()
    print("A conexão com o servidor foi finalizada")
