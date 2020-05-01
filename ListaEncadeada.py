
class Node:
    
    def __init__(self, value, next_node = None):
        self.__value = value
        self.next_node = next_node
        
    @property
    def value(self):
        return self.__value


class LinkedList:
    
    def __init__(self):
        self.__main_node = None

    #para adicionar um elemento na lista, verifica se a posição é vazia, se for, insere, se não usa o ponteiro e aponta para o proximo até encontrar uma posição vazia    
    def append(self, value):
        if self.__main_node is None:
            self.__main_node = Node(value)
            return

        curr_node = self.__main_node
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node
        curr_node.next_node = Node(value)

    #para remover, igual o de adicionar, deve-se verificar se há um elemento na posição, se tiver, elimina o e o anterior aponta para o proximo não vazio
    def remove(self, value):
        if self.__main_node is None:
            return

        left_node = None
        curr_node = self.__main_node

        if curr_node.value == value:
            self.__main_node = curr_node.next_node

        while True:
            left_node = curr_node
            curr_node = curr_node.next_node

            if curr_node is None:
                break

            if curr_node.value == value:
                left_node.next_node = curr_node.next_node

#para exibir, usa-se um enquanto para percorrer a lista e imprimir no terminal
    def show(self):
        values = []
        curr_node = self.__main_node
        while curr_node is not None:
            values.append(curr_node.value)
            curr_node = curr_node.next_node
        print("Lista: {}".format(values))


def main():
    linked_list = LinkedList()

    print("Inserindo elementos na lista e exibindo")
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    linked_list.show()

    print("removendo do meio da lista")
    linked_list.remove(2)

    linked_list.show()

    print("Removendo todos os itens da lista")
    linked_list.remove(1)
    linked_list.remove(3)

    linked_list.show()

    print("Inserir um elemento na lista vazia")
    linked_list.append(10)

    linked_list.show()

if __name__ == "__main__":
    main()