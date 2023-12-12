import json
from classes import *
from db import *

# JSON_FILE = 'C:/Users/marsh/Desktop/FACULDADE/P3/frostbook/prompt_app/users.json'
# user_list_file = open(JSON_FILE)
# user_list = json.load(user_list_file)

def welcome():
    print('1 -> Logar\n2 -> Criar uma conta\n3 -> Sair')
    welcome_answer = input('Escolha sua opção:')
    if welcome_answer == '1': 
        user = login()
        return user
        
    if welcome_answer == '2':
            try:
                create_user(Profile)
                welcome()
            except NameError:
                print("Você não está logado")
                welcome()

    if welcome_answer == '3':
        print('Saindo')
        return False

def create_user(Profile):
    username = input('Digite o nome do usuário: ')
    if general_search('username','username',username) !=0:
        print('Usuário já existe')
        return 
    first_name = input('Primeiro nome: ')
    second_name = input('Segundo nome: ')
    password = input('Senha: ')
    bday = input('Data de Nascimento: ')
    email = input('Digite seu email: ')
    gender = input('Genero: ')
    if general_search('username','email',email):
        print('Usuário já existe')
        return  
    user = Profile(username,first_name,second_name,password,bday,email,gender)
    insert_user(user)
    return user


def create_post(Posts,Profile):
    post = input('O que deseja postar? ')
    post = Posts(Profile,content=post,image=None, like_count = 0 ,comments = None)
    userid = general_search('userid','username',Profile.username)
    # post = vars(post)
    insert_post(userid,post)
    # save_users(Profile)

def view_post(Profile):
    n_post = (len(Profile.posts))
    if n_post == 0:
        print("Você não tem nenhum post")
    else:
        for posts in Profile.posts:
            print(f"{posts['content']} -> Curtidas: {posts['like_count']} -> Comentários: {posts['comments']}\n")
    return

def see_folows(Profile):
    n_follows = general_search('followers','username',Profile.username)
    print(n_follows)
    if n_follows == 0:
        print("Você não segue ninguém")
    else:
        print('Lista de pessoas que você segue ')

def add_follow(Profile):
    list_users()
    select = input("Que usuário deseja seguir? ")
    if select != Profile.username:
        insert_follower(Profile.username,select)
        # save_users(Profile)
        return
    elif select == Profile.username:
        print("Você não pode seguir a si próprio")
    else:
        print('Usuário não encontrado')

def login():
    username = input('Usuário: ')
    password = input('Senha: ')
    user = login_user(username,password)
    return user

def menu(Profile):
    menu_options = ['Criar post','Ver posts','Listar Seguindo','Seguir usuários','Sair']
    while True:
        for n in range(0,5):
            print(f"{n+1} - {menu_options[n]}")
        choice = input("O que deseja fazer? ")
        if choice == '1':
            return create_post(Posts,Profile)
        elif choice == '2':
            return view_post(Profile)
        elif choice == '3':
            return see_folows(Profile)
        elif choice == '4':
            return add_follow(Profile)
        elif choice == '5':
            print('Saindo')
            return False
    

# def save_users(Profile):
#     save = vars(Profile)
#     user_list['users'][Profile.username] = save
#     with open(JSON_FILE,'w',encoding='utf-8') as save_user:
#         json.dump(user_list, save_user)
#     return Profile
