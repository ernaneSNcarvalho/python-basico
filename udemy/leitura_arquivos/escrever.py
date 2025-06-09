# r = read
# w = write
# a = append
# x = create

lista = ["Joao\n", "Pedro\n", "Paulo\n"]

arquivo = open("lista.txt", "w")  # sobrescreve o conteudo
# arquivo.write("teste")
arquivo.writelines(lista)

arquivo.close()
