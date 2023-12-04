from functions import *

welcome()

while True:
    welcome_answer = input('Digite L para ver o Logar | Digite C para criar uma conta | Digite M para ver o Menu | Digite Q para sair ')
    if welcome_answer == 'm':
        menu(user)
    if welcome_answer == 'l':
        user = login()

    elif welcome_answer == 'c':
        user = create_user(Profile)
        print('Usuário criado com sucesso')
        print(f'username : {user.username}')

    elif welcome_answer == 'q':
        print('Até a próxima')
        break

