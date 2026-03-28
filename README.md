# 🛡️ Ferramenta de Análise de Logs e Scan de Rede (CLI)

## 📌 Sobre o Projeto
Uma ferramenta de interface de linha de comando (CLI) desenvolvida em Python para auxiliar em tarefas diárias de infraestrutura e cibersegurança. O sistema é dividido em dois módulos operacionais que permitem diagnosticar a exposição de servidores na rede e identificar rapidamente potenciais ameaças em arquivos de log.

## 🚀 Tecnologias e Bibliotecas Utilizadas
* **Python 3**
* `argparse`: Para a construção e roteamento da interface de linha de comando.
* `re` (Expressões Regulares): Para extração e validação de padrões (endereços IPv4) em grandes volumes de texto.
* `socket`: Para testes de conectividade TCP em baixo nível.

## ⚙️ Funcionalidades
1. **Módulo de Redes (Port Scanner):** - Estabelece conexões TCP rápidas com um IP alvo para verificar a disponibilidade de portas críticas e serviços essenciais (21/FTP, 22/SSH, 80/HTTP, 443/HTTPS, 8080).
2. **Módulo de Segurança (Log Analyzer):** - Realiza a leitura otimizada de arquivos de log do servidor.
   - Filtra eventos críticos marcados com a tag `[ERRO]`.
   - Utiliza Regex para extrair automaticamente o endereço IP de origem do possível atacante, gerando um alerta de segurança imediato.

## 🕹️ Como Executar
1. **Para rodar o Scanner de Rede:** python -m src.ferramenta --ip <IP_DO_ALVO> ex:127.0.0.1
2. **Para rodar o Analisador de Logs de Segurança:** python -m src.ferramenta --log <CAMINHO_DO_ARQUIVO> ex:log_servidor.txt
