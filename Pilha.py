
class Stack:
    
    def __init__(self):
        self.__stack = []
    #insere no topo    
    def push(self, value):
        self.__stack.append(value)
    #retira do topo    
    def pop(self):
        return self.__stack.pop()
        
    def show(self):
        print("Pilha: {}".format(self.__stack))


def main():
    stack = Stack()

    print("Insere os elementos na pilha")
    stack.push(4)
    stack.push(5)
    
    stack.show()

    print("Retira 1 elemento da pilha")
    stack.pop()

    stack.show()


if __name__ == "__main__":
    main()
