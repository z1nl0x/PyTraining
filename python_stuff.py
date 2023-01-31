
####################################################
# If Statements
####################################################

# x = int(input('Por favor, entre com um número inteiro: '))

# if x < 0:
#     x = 0
#     print('Negativo se tornou Zero!')
# elif x == 0:
#     print('Zero!')
# elif x == 1:
#     print('Um!')
# else:
#     print('Mais que Um!')


####################################################
# For Statements
####################################################

# palavras = ['gato', 'janela', 'cachorro']

# for p in palavras:
#     print(p, len(p))


# # Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', 'Maria': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)

# for i in range(5):
#     print(i)

# print(list(range(5, 10)))

# print(list(range(0, 10, 3)))

# print(list(range(-10, -100, -30)))

# a = ['teste1', 'teste2', 'teste3', 'teste4']

# for i in range(len(a)):
#     print(i, a[i])

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'igual', x, '*', n//x)
#             break
#     else:
#         print(n, 'é número primo')

# for num in range(2, 10):
#     if num % 2 == 0:
#         print(num, 'Número par encontrado!')
#         continue
#     print(num, 'Número impar encontrado!')

####################################################
# Match Statements
####################################################

# def http_error(status):
#     match status:
#         case 400:
#             return print('Bad Request!')
#         case 404:
#             return print('Not found!')
#         case 418:
#             return print("I'm a teapot!")
#         case _:
#             return print('Algo deu errado com a internet!')

# http_error(404)

