class List:
    def __init__(self, nome):
        self._filename = f"{nome}.txt"

    def get_list(self):
        list = []
        with open(self._filename, "r") as file:
            for item in file:
                list.append(item.strip())
            return list

    def add_item(self, new_item):
        with open(self._filename, "a") as file:
            if new_item != "":
                file.write(f"{new_item}\n")
                return True
            else:
                return False


list = List("lista")
for item in list.get_list():
    print(f"- {item}")

print("------------")

new_item = input("Digite o novo item: ")
added = list.add_item(new_item)

if added == True:
    print("Item adicionado com sucesso.")
else:
    print("Não houve nenhuyma adição.")
