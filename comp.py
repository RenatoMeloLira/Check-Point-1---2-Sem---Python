import hashlib

file_0 = input("Escolha o arquivo original de backup: ")
file_1 = input("Escolha o arquivo para a comparação: ")

hash_0 = hashlib.new('sha256')
hash_0.update(open(file_0, 'rb').read())

hash_1 = hashlib.new('sha256')
hash_1.update(open(file_1, 'rb').read())

if hash_0.digest() != hash_1.digest():
    pergunta = input("O arquivo não esta integro, voce deseja restaurar a configuração original? ").upper()
    if pergunta == "SIM":
        arquivo = open(file_0, 'r') # Abra o arquivo (leitura)
        conteudo = arquivo.readlines()
        arquivo.close()
        arquivo = open(file_1, 'w') # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
        arquivo.close()
        print("Arquivo restaurado com sucesso!")
else:
    print("O arquivo esta integro.")
