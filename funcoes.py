# Funções - DRY - Dont repeat yourself


def boas_vindas1():
    print("isso é uma funcao")
    print("basta chamala")

boas_vindas1()

# Criando uma funcao de soma

def soma():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)

soma()



# Parametros e argumentos em uma funcao

def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', 3)
boas_vindas('Felipe', 5)
boas_vindas('Ronaldo', 4)


'''
def boas_vindas_felipe():
    print("Olá Felipe")
    print("Temos 5 laptops em estoque")


def boas_vindas_ronaldo():
    print("Olá Ronaldo")
    print("Temos 4 laptops em estoque")


def boas_vindas_marcos():
    print("Olá marcos")
    print("Temos 3 laptops em estoque")


boas_vindas_felipe()
boas_vindas_marcos()
boas_vindas_ronaldo()
'''


#Funcoes 
    # Parametro -> argumento 
    # Default = Aquele que voce define o valor no parametro
    # Non-default = Aquele que vc nao define o valor no parametro

def boas_vindas3(nome, quantidade = 6):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas3('Felipe')



# Print ou return em funcoes

def cliente1(nome):
    print(f'Ola {nome}')


def cliente2(nome):
    return f'Ola {nome}'


x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)


# Varios argumentos xargs com numeros
# Criar uma funcao que soma varios numeros

def somar_valores(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = somar_valores(2, 3, 4, 7)

print(x)


# Varios argumentos xargs nomeando parametros 
# Criar uma funcao que armazena numeros e strings (dados)

def agencia(**carro):
    return carro

print(agencia(marca = 'Gol', cor = 'Branca', motor = 1.0))

