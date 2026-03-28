import argparse
from src import leitor
from src import scanner

parser = argparse.ArgumentParser(description='Ferramenta de Análise de Logs e Scan de Rede')

parser.add_argument('--ip', type=str, help='Digite o IP que deseja escanear')

parser.add_argument('--log', type=str, help='Caminho do arquivo de log para análise')

argumentos = parser.parse_args()

if argumentos.ip:
    print(f"[*] Iniciando módulo de REDES. Escaneando o IP: {argumentos.ip}")
    scanner.scanner_ip(argumentos.ip)
elif argumentos.log:
     print(f"[*] Iniciando módulo de SEGURANÇA. Analisando o arquivo: {argumentos.log}")
     leitor.leitor_log(argumentos.log)
else:
    print("[!] Erro de uso. Você precisa escolher uma ação.")
    print("Exemplos de uso:")
    print("  python ferramenta.py --ip 127.0.0.1")
    print("  python ferramenta.py --log log_servidor.txt")