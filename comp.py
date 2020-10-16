
file_0 = input("Escolha o arquivo original de backup: ")
file_1 = input("Escolha o arquivo para a comparação: ")

var1 = (open(file_0, 'r').read())

var2 = (open(file_1, 'r').read())

if var1 != var2:
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
