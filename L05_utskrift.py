# fall 1
# def utskrift(lista):
#     if len(lista) > 0:
#         print(lista[0])
#         utskrift(lista[1:])

# fall 2
def utskrift(lista):
    if len(lista) > 0:
        utskrift(lista[1:])
        print(lista[0])


utskrift([1, 2, 3, 4, 5])
