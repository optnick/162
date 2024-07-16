Programa para monitorar a carteira 162 do canal Investidor Internacional
Link do canal: https://www.youtube.com/@investidorint
Link do vídeo: https://www.youtube.com/watch?v=Xe1w-AfL6qQ&ab_channel=InvestidorInternacional

Foi feito em python. 
Foi usada a API BlockCypher, que é de graça, dá 1000 consultas por dia, 100 consultas por hora. 

Dependência:
```bash
pip install requests
```

![image](https://github.com/user-attachments/assets/1d8b1281-3b32-4e52-a4d0-207504d3b7bc)

O programa pega automaticamente a chave pública, que é quando gasta "input". No caso dessa transação, ele pegou somente a chave pública da carteira que enviou para a do puzzle, ou seja pegou a chave pública da carteira 
bc1q5a3ak3vlmsawfptv99pvmxzv4qxvg7aj7re48g que é 0349cf89f7e476a8a8b36a8816addad3ea5381c69bb67782d941ec7ac342e1ab7e, mas como o programa não "viu" o input da carteira do puzzle "19L9vivFCPJnAVDsjZ76mF2ZiTLKFUXEpV", não printou a pub key, só vai acontecer quando encontrar o input correto.

Obs.: Quando forem usar o BSGS, se quiserem encontrar realmente, precisam ter no mínimo 64 GBs de RAM, pois mesmo com 32 Gbs ou menos, percorrer um range com apenas 30 Petakeys é inviável, antes que a transação seja feita, sendo que o range são de 66 bits, ou seja, demoraria mais de 40 minutos para percorrer os 66 bits. 
