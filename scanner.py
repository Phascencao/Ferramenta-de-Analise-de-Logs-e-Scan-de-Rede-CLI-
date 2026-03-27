import socket


def scanner_ip(ip_alvo):
    portas_alvo = [21, 22, 80, 443, 8080]

    for porta in portas_alvo:

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        cliente.settimeout(1)

        resultado = cliente.connect_ex((ip_alvo, porta))

        if resultado == 0:
            print(f"Resultado: A porta {porta} no IP {ip_alvo} está ABERTA!")
        else:
            print(f"Resultado: A porta {porta} no IP {ip_alvo} está FECHADA ou bloqueada.")

        cliente.close()