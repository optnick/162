import requests
import time

# Substitua pela sua chave de API do BlockCypher
API_TOKEN = 'Seu_Token_da_blockcypher'
WALLET_ADDRESS = '19L9vivFCPJnAVDsjZ76mF2ZiTLKFUXEpV'

def get_latest_transactions(address):
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/full?token={API_TOKEN}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro ao acessar a API: {response.status_code}, Mensagem: {response.text}')
        return {}

def monitor_wallet():
    last_tx_hash = None
    while True:
        data = get_latest_transactions(WALLET_ADDRESS)
        transactions = data.get('txs', [])
        if transactions:
            latest_tx = transactions[0]
            if latest_tx['hash'] != last_tx_hash:
                last_tx_hash = latest_tx['hash']
                print(f'Nova transação detectada: {latest_tx}')
                
                # Verifica se o endereço monitorado é um input e printa a chave pública
                for input in latest_tx.get('inputs', []):
                    input_addresses = input.get('addresses', [])
                    if WALLET_ADDRESS in input_addresses:
                        witnesses = input.get('witness', [])
                        for witness in witnesses:
                            print(f'Chave Pública do endereço {WALLET_ADDRESS}: {witness}')
        
        time.sleep(10)  # Espera 10 segundos antes de verificar novamente.

if __name__ == "__main__":
    monitor_wallet()