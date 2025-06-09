# r = read
# w = write
# a = append
# x = create

arquivo = open("lista.txt", "r")
linhas = arquivo.readlines()

for linha in linhas:
    print(
        f"Linha: {linha.strip()}"
    )  # strip limpa as quebras de linhas e espaços inuteis
