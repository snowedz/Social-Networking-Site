from functions import *

welcome()

welcome_answer = input('Digite Y para Sim | Digite N para criar uma conta | Digite Q para sair ')

print(f"Welcome Answer: {welcome_answer}")

if welcome_answer == 'y':
    list_users()

elif welcome_answer == 'n':
    user = create_user(Profile)
    print('Usuário criado com sucesso')
    print(f'usuario: {user.username}')

elif welcome_answer == 'q':
    print('Até a próxima')
    pass

