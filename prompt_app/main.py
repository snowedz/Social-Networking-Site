from functions import *
print('\n')
print('-------------Bem vindo ao FrostBook-------------\n')
print('-> Já tem uma conta?')
user = welcome()
while user != False:
    user = menu(user)

