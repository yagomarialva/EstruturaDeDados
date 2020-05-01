import random

class Queue:
    
    def __init__(self):
        self.__queue = []

    #insere um item na fila
    def enqueue(self, value):
        self.__queue.append(value)

    #retira do topo da fila    
    def dequeue(self):
        return self.__queue.pop(0)
        
    def show(self):
        print("Fila: {}".format(self.__queue))

def main():
    queue = Queue()

    print("insere 4 elementos aleatorios na fila")

    for _ in xrange(0, 4):
        queue.enqueue(random.randint(10,99))

    queue.show()
    print("remove 1 elemento da fila")
    queue.dequeue()
    queue.show()
    print("remove outro elemento da fila")
    queue.dequeue()

    queue.show()

if __name__ == "__main__":
    main()