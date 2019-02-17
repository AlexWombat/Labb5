from bintreeFile import Bintree
from string import ascii_lowercase
from linkedQFile import LinkedQ


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent                # noden pekar på sin förälder


class SolutionFound(Exception):
    pass


def makechildren(parent, startord, slutord, svenska, q, gamla):
    alfabet_lista = list(ascii_lowercase)
    alfabet_lista.extend(['å', 'ä', 'ö'])                   # lista med alla bokstäver i alfabetet
    nya_ord = []
    gamla.put(parent.word)
    for i in range(0, 3):
        bokstavslista = list(parent.word)
        for j in alfabet_lista:
            bokstavslista[i] = j                            # en bokstav byts ut i taget
            nya_ord.append(''.join(bokstavslista))          # de nya "orden" läggs in i en lista
    for i in nya_ord:
        if i in svenska and i not in gamla:                 # finns orden i ordlistan och är de dumbarn?
            children = ParentNode(i, parent)
            q.enqueue(children)
            if i == slutord:
                print('Kortaste ordkedjan från', '\033[4m' + startord + '\033[0m', 'till', '\033[4m' + slutord + '\033[0m', 'ges av följande:')
                print(startord)
                q.writechain(children)
                raise SolutionFound
            else:
                gamla.put(i)


def main():
    svenska = Bintree()
    gamla = Bintree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet not in svenska:
                svenska.put(ordet)
    startord = input('Ange ett startord: ')
    parent = ParentNode(startord)
    slutord = input('Ange ett slutord: ')
    q = LinkedQ()
    q.enqueue(parent)
    try:
        while not q.isEmpty():
            parent = q.dequeue()
            makechildren(parent, startord, slutord, svenska, q, gamla)
        print('Det finns ingen väg.')
    except SolutionFound:
        pass


main()
