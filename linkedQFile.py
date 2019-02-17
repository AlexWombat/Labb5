class Node:
    def __init__(self, value, next=None):
        self.card = value
        self.next = next


class LinkedQ:
    def __init__(self):
        self.__first = None       # två understreck för privata variabler
        self.__last = None

    def enqueue(self, value):
        new = Node(value)
        if self.__first is None:
            self.__first = new
            self.__last = new
        else:
            self.__last.next = new
            self.__last = new

    def dequeue(self):
        v = self.__first.card
        self.__first = self.__first.next
        return v

    def writechain(self, child):
        if child.parent:
            self.writechain(child.parent)
            print(child.word)                  # skriver ut kedjan från startord till slutord

    def isEmpty(self):
        return self.__first is None
