
## Criando tuplas

vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')
print(vendas)

# acessando un valor de uma tupla

nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]
print(salario)

nome, data_contratacao, data_nascimento, salario, cargo = vendas
print(salario)


## O enumerate que vinha usamos ate agora, na verdade, cria uma tupla para a gente. Vamos ver na pratica.

vendas = [1000, 2000, 300, 300, 150]
funcionarios= ['João', 'Lira', 'Ana', 'Maria', 'Paula']

for i, venda in enumerate(vendas):
    print('{} vendeu {}'.format(funcionarios[i], venda))

print('---------------------------')

#transformando tuplas em lista
lista1 = list(vendas)
print(lista1)


# Vamos ver o tamnho da lista
tamanho = len(vendas)
print(tamanho)

i = funcionarios.index('Lira')
print(i)
