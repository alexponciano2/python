# nome = input('Digite seu nome: ')
# sobrenome = input('Digite seu ultimo sobrenome: ')
# cpf = input('Digite seu CPF: ')
# endereco = input('Digite seu endereço: ')
# idade = input('Digite sua idade: ')
# altura = input('Digite sua altura: ')
# telefone = input('Digite seu telefone: ')

# print('Cadastro do Senhor', nome, 'concluído com sucesso!', '\n' 'Senhor', nome, sobrenome,'\n' 'CPF:', cpf,'\n' 'Idade:', idade, 'anos','\n' 'Altura:', altura,'\n' 'Telefone:', telefone,'\n' 'Residente no endereço:', endereco)
# ------------------------------------------------------------------------
# a = 50
# b = 30
# fruta = input("digite uma fruta inciado com a letra A: ")

# if a > b and fruta == 'abacaxi':
#     print(a, "é maior do que", b, "e a fruta é", fruta)
# else:
#     print("deu ruim teu IF")
# ------------------------------------------------------------------------
# print('MENU: \n1 = Escreve Guilherme\n2 = Escreve João\n3 = Escreve Maria\n')

# opcao = input("Escolha uma opção: ")

# if opcao == '1':
#     print('Você escolheu: Guilherme\n')
# elif opcao == '2':
#     print('Você escolheu: João\n')
# elif opcao == '3':
#     print('Você escolheu: Maria\n')
# else:
#     print('Opção inválida!\n')
# ------------------------------------------------------------------------
# idade = input("Digite sua idade: ")
# peso = input("Digite seu peso: ")
# altura = input("Digite sua altura em centímetros: ")

# if int(idade) >= 18 and int(peso) >= 60 and int(altura) >= 170:
#     print("Pode entrar no exército!")
# else:
#     print("Não pode entrar no exército!")
# ------------------------------------------------------------------------
# lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']

# lista_nomes.append('ALEX')
# lista_nomes.remove('Maria')
# lista_nomes.insert(1, 'Helena')

# contador_Alex = lista_nomes.count('ALEX')

# print(lista_nomes.lower())
# ------------------------------------------------------------------------
# nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']

# for i in nomes:
#     print(i)
# ------------------------------------------------------------------------
# nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']

# for i in range(len(nomes)):
#     print(nomes[i])
# ------------------------------------------------------------------------
# palavra = 'Guilherme Junqueira'

# for i in palavra:
#     print(i)
# ------------------------------------------------------------------------
# i = 0
# while i < 10:
#     print('i ainda é menor do que 10: ', i)
#     i = i + 1

# print('Acabou o While, seu "i" agora vale:', i)
# ------------------------------------------------------------------------
# numero = 0
# while True:
#     print(numero)
#     if numero == 20:
#         break
#     numero += 1
# ------------------------------------------------------------------------
# EXERCÍCIO:

# quantidade_de_pessoas = int(input('Quantas pessoas virão à festa?: '))

# lista_de_convidados = []

# for i in range(quantidade_de_pessoas):
#     nome = input('Qual o nome do convidado?: ')
#     lista_de_convidados.append(nome)
   
# print('Os convidados para a festa são: ', lista_de_convidados)
# ------------------------------------------------------------------------
# ESTRUTURA DE DADOS
minha_lista =    ['Gui', 'Joao']                       # List
minha_tupla =    ('Gui', 'Joao')                       # Não é mutável, a não ser que seja ela toda
meu_dicionario = {'nome': 'Guilherme', 'idade': 27}    # Key + Value
meu_conjunto =   {'Gui', 'Joao'}                       # Não tem Key, Não tem itens repetidos, Não tem índice