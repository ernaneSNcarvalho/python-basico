## transformar lista de tarefas em poo e escrita em arquivo txt

tarefas = []


def menu():
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefas")
    print("4. Deletar Tarefas completadas")
    print("5. Sair")


def inserir(descricao):
    tarefas.append(descricao)


def atualizar(id, descricao):
    tarefas[id] = descricao


def deletar(id):
    del tarefas[id]


print("Menu do gerenciador de tarefas!")

menu()
opcao = int(input("Digite a opção desejada: "))

while opcao != 5:
    match opcao:
        case 1:
            descricao = input("Insira a tarefa a ser adicionada: ")
            inserir(descricao)
            print(f"Tarefa adicionada: {descricao}")
        case 2:
            for tarefa in tarefas:
                print(tarefa)
        case 3:
            # Mostra todas as tarefas numeradas
            for i, tarefa in enumerate(tarefas):
                print(f"{i} - {tarefa}")

            # Pede o id para atualizar, fora do for
            id = int(input("Digite a chave a ser atualizada: "))

            # Valida o id para garantir que está dentro da lista
            while id < 0 or id >= len(tarefas):
                print("Insira um valor válido da lista.")
                id = int(input("Digite a chave a ser atualizada: "))

            descricao = input("Descreva a nova tarefa: ")
            atualizar(id, descricao)
        case 4:
            id = int(input("Digite a chave a ser atualizada: "))
            for i, tarefa in enumerate(tarefas):
                print(f"{i} - {tarefa}")
                while id != id:
                    print("Insira um valor da lista.")
                    id = int(input("Digite a chave a ser completada: "))
            deletar(id)
            print(f"Tarefa Deletada: {tarefas[id]}")
    opcao = int(input("Digite a opção desejada: "))


print("Saiu do programa!")
