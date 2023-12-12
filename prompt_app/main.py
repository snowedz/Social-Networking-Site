from functions import *

print('Bem vindo ao FrostBook')
print('Já tem uma conta?\n')
user = welcome()
while user != False:
    user = menu(user)

