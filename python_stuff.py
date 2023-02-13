
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
    # match status:
    #     case 400:
    #         return print('Bad Request!')
    #     case 404:
    #         return print('Not found!')
    #     case 418:
    #         return print("I'm a teapot!")
    #     case _:
    #         return print('Algo deu errado com a internet!')
        
# http_error(404)


# def match_point(x, y):
#     point = (x, y)
#     match point:
#         case (0, 0):
#             print('Origin')
#         case (0, y):
#             print(f'Y={y}')
#         case (x, 0):
#             print(f'X={x}')
#         case (x, y):
#             print(f'X={x}, Y={y}')
#         case _:
#             raise ValueError('Not a point!')
        
# match_point(0, 1)

# class Point:
#     x: int
#     y: int

# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print('Origin')
#         case Point(x=0, y=y):
#             print(f'Y={y}')
#         case Point(x=x, y=0):
#             print(f'X={x}')
#         case Point():
#             print('Somewhere else!')
#         case _:
#             print('Not a point')

# Point(1, 0)

# from enum import Enum

# class Color(Enum):
#     RED = 'red'
#     GREEN ='green'
#     BLUE = 'blue'


# color = Color(input('Enter your choice of "red", "blue" or "green": '))

# match color:
#     case Color.RED:
#         print('I See red!')
#     case Color.GREEN:
#         print('Grass is green')
#     case Color.BLUE:
#         print("I'm feeling the blues :(")

# def fib(n):
#     """ Print a Fibonacci series up to n. """
#     a, b = 0, 1
#     while a < n:
#         print(a, end= ' ')
#         a, b = b, a + b
#     print()

# fib(2000)


# def fib2(n):
#     """ Return a list containing the Fibonacci series up to n. """
#     result = []
#     a, b = 0, 1

#     while a < n:
#         result.append(a)
#         a, b = b, a + b
#     return print(result)

# f100 = fib2(100)
# f100

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('Invalid user response')
#         print(reminder)

# ask_ok('Do you really want to quit?')

# i = 5

# def f(arg=i):
#     print(arg)

# i = 6
# f()


# def f(a, L=[]):
#     L.append(a)
#     return L

# # def f(a, L=None):
# #     if L is None:
# #         L = []
# #     L.append(a)
# #     return L

# print(f(1))
# print(f(2))
# print(f(3))

"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
"""
#########################################################
"""
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

"""
"""
    Function Annotations:

    Function annotations are completely optional metadata information about the types used by 
    user-defined functions (see PEP 3107 and PEP 484 for more information).
"""

# def f(ham: str, eggs: str = 'eggs' ) -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + 'and' + eggs

# f('spam')

"""
    Intermezzo: Coding Style

     - Use 4-space indentation, and no tabs.

     - 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.

     - Wrap lines so that they don’t exceed 79 characters.

     - This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.

     - Use blank lines to separate functions and classes, and larger blocks of code inside functions.

     - When possible, put comments on a line of their own.

     - Use docstrings.

     - Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).

     - Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods. Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).

     - Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8, or even plain ASCII work best in any case.

     - Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.
"""




