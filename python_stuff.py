
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