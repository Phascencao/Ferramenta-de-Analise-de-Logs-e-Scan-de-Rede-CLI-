import re #regex, biblioteca importante para procurar padrões

def leitor_log(log_servidor):
    ip_padrao = r'\d+\.\d+\.\d+\.\d+'

    with open(log_servidor, 'r', encoding='utf-8') as arquivo:

        for linha in arquivo:
            if '[ERRO]' in linha:
                ips_encontrados = re.findall(ip_padrao, linha)
                if ips_encontrados:
                    print(f'ALERTA DE SEGURANÇA: Ataque vindo do ip {ips_encontrados} ')