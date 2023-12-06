from functions import *

welcome()

while True:
    welcome_answer = input('Digite L para ver o Logar | Digite C para criar uma conta | Digite M para ver o Menu | Digite Q para sair ')
    
    if welcome_answer == 'm' or welcome_answer == 'M':
        try:
            menu(user)
        except NameError:
            print("Você não está logado")
    if welcome_answer == 'l' or welcome_answer == 'L':
       user = login()
       print("\nUsuário Logado\n")

    elif welcome_answer == 'c' or welcome_answer == 'C':
         user = create_user(Profile)
         print('Usuário criado com sucesso')
         print(f'username : {user.username}')

    elif welcome_answer == 'q' or welcome_answer == 'Q':
        print('Até a próxima')
        break

