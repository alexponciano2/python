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
lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']

lista_nomes.append('ALEX')
lista_nomes.remove('Maria')
lista_nomes.insert(1, 'Helena')

# contador_Alex = lista_nomes.count('ALEX')

print(lista_nomes.lower())
