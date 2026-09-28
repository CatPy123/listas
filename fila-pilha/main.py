from pilha import Pilha
from fila import Fila

# enfileirar 
enfileirando = Fila()
enfileirando.enfileirar(1)
enfileirando.enfileirar(2)
enfileirando.enfileirar(3)
enfileirando.enfileirar(4)

# mostrar a fila
print("Fila: ", enfileirando.exibir()) 

# desenfileirar 
while not enfileirando.esta_vazia():
    itens = enfileirando.desenfileirar()
    print("Item: ", itens)

# mostrar a fila
print("Fila após desenfileirar: ", enfileirando.exibir())

# empilhar
empilhando = Pilha()
empilhando.empilhar(10)
empilhando.empilhar(20)
empilhando.empilhar(30)
empilhando.empilhar(40)

# mostrar a pilha 
print("Pilha: ", empilhando.exibir())

# desempilhar 
while not empilhando.esta_vazia():
    itens_pilha = empilhando.desempilhar()
    print ("Itens: ", itens_pilha)

# mostrar a pilha
print("Pilha após desempilhar: ", empilhando.exibir())
